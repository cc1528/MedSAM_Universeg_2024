# Medical Image Segmentation with MedSAM and UniverSeg

**MSc Data Science Thesis. University of Amsterdam, 2024**

## Motivation

Accurate medical image segmentation is essential for identifying anatomical structures and supporting medical image analysis. However, segmentation models can face challenges when working with limited annotated data, variations in image quality, and differences in anatomical appearance.

Foundation models such as MedSAM and few-shot segmentation approaches such as UniverSeg offer different ways of addressing these challenges.

This thesis investigates their performance on ultrasound images of the fetal head and pubic symphysis, with particular attention to whether selecting representative support examples can improve segmentation results.

## Research Objectives

The project focuses on two main objectives:

1. **Model comparison:** Evaluate MedSAM and UniverSeg for medical ultrasound image segmentation.
2. **Support set selection:** Investigate whether feature-based clustering can help select more representative support images for UniverSeg.

## Methodology

The research involved:

- **MedSAM:** Applying a pretrained medical image segmentation model and evaluating its predictions.
- **UniverSeg:** Investigating few-shot segmentation using support images and corresponding masks.
- **Feature extraction:** Using U-Net-based representations to characterize medical images.
- **Dimensionality reduction:** Applying UMAP to explore feature representations.
- **Clustering:** Using K-means to investigate support set selection.
- **Evaluation:** Comparing segmentation performance using quantitative metrics and visual inspection.

## Main Findings

MedSAM achieved better overall segmentation performance than UniverSeg on the evaluated dataset.

The clustering-based support set selection approach did not improve segmentation of the main anatomical structures. These findings highlight the challenges of selecting informative support examples and motivate further investigation into how image characteristics and feature representations influence segmentation performance.

## Repository Contents

The repository contains the implementations and experimental code used in the thesis.

### Additional Data Exploration

The [`eda_data_extraction/`](https://github.com/cc1528/MedSAM_Universeg_2024/blob/main/datasets/eda_data_extraction.py) folder contains an archived Python script from earlier exploratory work.

The script demonstrates how structured MATLAB medical imaging files were used to extract ultrasound frames and anatomical contour annotations and generate PNG visualizations.


## Thesis

The complete research methodology, experimental setup, quantitative results, and discussion are documented in the MSc Data Science thesis (2024).
