# Project Scope

## Project Title
Explainable Brain Tumor Segmentation and Quantitative Analysis Using TransUNet and Attention U-Net

## Locked Core Decisions

### Task and Training Design
- Task type: Binary tumor segmentation
- Training pipeline: 2D slice-based
- Demo framework: Streamlit

### Dataset Decision
- Primary dataset for the project: **BraTS 2020 Training Dataset**
- Reason for selection:
  - sufficient for binary brain tumor segmentation
  - easier to use for a 2D slice-based mini-project pipeline
  - contains the required MRI modalities and segmentation masks
  - simpler and more practical than using a newer challenge setup for the first full build

### Input Modalities
- FLAIR
- T1ce
- T2
- T1 excluded from the initial build

### Binary Mask Mapping Rule
The original BraTS multiclass segmentation mask will be converted into a **binary whole-tumor mask** using the following rule:

- `0 -> 0` (background)
- `1 -> 1` (tumor)
- `2 -> 1` (tumor)
- `4 -> 1` (tumor)

Equivalent implementation rule:
- **binary_mask = (original_mask > 0)**

Interpretation:
- all non-zero BraTS tumor labels are merged into a single foreground class
- the final binary segmentation target represents the **whole tumor region**

## Planned Core Components
1. Data preprocessing pipeline for BraTS MRI scans
2. 2D slice extraction pipeline
3. Attention U-Net training pipeline
4. TransUNet training pipeline
5. Segmentation evaluation and model comparison
6. Explainability / heatmap visualization
7. Tumor area and estimated volume analysis
8. Streamlit demo interface

## Pending Phase 2 Decisions
The following implementation details will be finalized before preprocessing code is written:
1. exact 2D sample format and slice-selection strategy
2. patient-wise train/validation/test split strategy
3. exact deliverables required before Phase 3 begins