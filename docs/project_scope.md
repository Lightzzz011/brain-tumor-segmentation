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

### 2D Sample Format and Slice Strategy

#### Slice Plane
- Use **axial slices only**

#### Input Sample Format
Each processed input image sample will represent **one axial slice from one BraTS patient case**.

Input image specification:
- shape: **`[3, 224, 224]`**
- channel order:
  1. FLAIR
  2. T1ce
  3. T2

#### Target Mask Format
Each processed target mask will represent the binary whole-tumor mask for the same axial slice.

Target mask specification:
- shape: **`[1, 224, 224]`**
- values: **`0` or `1`**

#### Slice Retention Rule
For each patient volume:
1. convert the original BraTS mask to a binary whole-tumor mask
2. identify all axial slice indices where the binary mask contains at least one tumor pixel
3. let:
   - `first_tumor_slice = min(tumor_slice_indices)`
   - `last_tumor_slice = max(tumor_slice_indices)`
4. retain all axial slices from:
   - **2 slices before the first tumor-positive slice**
   - through
   - **2 slices after the last tumor-positive slice**
5. clip the retained range to valid volume boundaries when needed

Practical interpretation:
- keep the entire tumor-containing axial region
- include a small context margin around the tumor
- discard far-away empty slices outside this retained band

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
1. patient-wise train/validation/test split strategy
2. exact deliverables required before Phase 3 begins