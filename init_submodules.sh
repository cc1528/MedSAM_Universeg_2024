#!/bin/bash

# Ensure the script stops if any command fails
set -e

# Replace the submodule URLs with token-included URLs in .git/config
sed -i 's|https://github.com/cc1528/MedSAM.git|https://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@github.com/cc1528/MedSAM.git|' .git/config

sed -i 's|https://github.com/cc1528/UniverSeg-eda.git|https://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@github.com/cc1528/UniverSeg-eda.git|' .git/config

# Initialize and update submodules
git submodule update --init --recursive
