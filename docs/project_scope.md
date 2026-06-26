# Project Scope

## Project Title
Explainable Brain Tumor Segmentation and Quantitative Analysis Using TransUNet and Attention U-Net

## Locked Core Decisions

### Task and Training Design
- Task type: Binary tumor segmentation
- Training pipeline: 2D slice-based
- Demo framework: Streamlit

### Dataset Decision
- Primary dataset for the project: **Dataset:
BraTS Adult Glioma (GLI) Training Dataset
Distributed via the BraTS 2023 Synapse project.**
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

### Patient-wise Train / Validation / Test Split Strategy

#### Split Type
- Use a **patient-wise split**, never a slice-wise split

#### Split Percentages
- **70% train**
- **15% validation**
- **15% test**

#### Split Rules
- each BraTS patient case belongs to exactly one split
- all retained slices from a patient must remain in the same split
- no patient may appear in more than one split
- use a fixed random seed for reproducibility

#### Planned Split Files
The preprocessing pipeline will later generate and store patient-level split files at:

- `data/splits/train_patients.csv`
- `data/splits/val_patients.csv`
- `data/splits/test_patients.csv`

## Phase 2 Output Definition

Before Phase 3 begins, the project must have a fully frozen preprocessing and dataset design covering:

1. exact dataset choice
2. exact binary mask mapping rule
3. exact 2D sample format
4. exact slice-retention strategy
5. exact patient-wise split strategy

## Phase 3 Implementation Target

Phase 3 will implement the first actual data pipeline components:

1. BraTS 2020 raw data download and folder placement
2. raw data audit and metadata inspection
3. binary mask conversion logic
4. axial slice extraction using the locked slice-retention rule
5. processed 2D sample generation in the locked format
6. patient-wise split file generation
