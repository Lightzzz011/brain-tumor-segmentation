# Project Scope

## Project Title
Explainable Brain Tumor Segmentation and Quantitative Analysis Using TransUNet and Attention U-Net

## Locked Core Decisions
- Task type: Binary tumor segmentation
- Training pipeline: 2D slice-based
- Demo framework: Streamlit
- Preferred dataset: BraTS 2020 or BraTS 2021
- Input modalities: FLAIR + T1ce + T2
- T1 modality excluded from the initial build

## Planned Core Components
1. Data preprocessing pipeline for BraTS MRI scans
2. Attention U-Net training pipeline
3. TransUNet training pipeline
4. Segmentation evaluation and comparison
5. Explainability / heatmap visualization
6. Tumor area and volume analysis
7. Streamlit demo interface