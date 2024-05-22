from pathlib import Path
import pandas as pd
from db import save_db
from PIL import Image
import numpy as np
from tqdm import tqdm
import json


def subdirs(path: Path):
    return [d for d in path.iterdir() if d.is_dir()]


def get_ground(d: Path, i: str) -> bool:
    path_image = Path(f"{d}/image/{i}.png")
    path_mask = Path(f"{d}/mask/{i}_mask.png")
    path_emask = Path(f"{d}/mask_enhance/{i}_mask.png")
    return path_image.exists() & path_mask.exists() & path_emask.exists(), (
        path_image,
        path_mask,
        path_emask,
    )


def get_image_cell(path: Path) -> str:
    #   [display images](https://github.com/simonw/datasette-json-html)
    return json.dumps(
        {
            "img_src": base_url + str(path.relative_to(base_dir)),
            "href": base_url + str(path.relative_to(base_dir)),
            "width": 200,
        }
    )


if __name__ == "__main__":
    path = Path("./data/us_data")
    rows = []
    set_ids = subdirs(path)
    pbar = tqdm(set_ids, total=len(set_ids), ncols=80)
    for d in pbar:
        images = sorted([f.stem for f in (d / "image").glob("*.png")])
        for i in images:
            ok, (path_image, path_mask, path_emask) = get_ground(d, i)
            if not ok:
                raise FileNotFoundError(f"{path_image, path_mask, path_emask}")

            # Store reference to the images and masks
            base_url = "http://localhost:8002/"
            base_dir = Path("./data")
            row = {
                "set_id": d.stem,
                "set_path": str(d),
                "image": get_image_cell(path_image),
                "mask": get_image_cell(path_mask),
                "mask_enhance": get_image_cell(path_emask),
            }

            # Open files
            image = Image.open(path_image)
            mask = np.array(Image.open(path_mask))
            emask = np.array(Image.open(path_emask))

            # Save some statistics
            row["w"], row["h"] = image.size

            # Find proportion of labels in mask and enhanced mask
            u_mask = np.unique(mask)
            u_emask = np.unique(emask)

            w, h = image.size
            area = w * h
            row["unique_mask"] = str(u_mask)
            for mi in u_mask:
                row[f"mask-{mi}"] = np.sum(mask == mi) / area

            row["unique_mask_enhance"] = str(u_emask)
            for ei in u_emask:
                row[f"mask_enhance-{ei}"] = np.sum(emask == ei) / area

            rows.append(row)

    df = pd.DataFrame(rows)
    save_db(df, "./data/files.db", "files", verbose=True)
