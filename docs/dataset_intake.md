# Dataset Intake Plan

## Selected Dataset
- **BraTS 2020 Training Dataset**

## Official Access Route
BraTS 2020 data access should be requested using the official BraTS / CBICA process.

Reference pages:
- BraTS 2020 Data page
- BraTS 2020 Registration / Data Request page
- CBICA Image Processing Portal (IPP)

## Raw Dataset Storage Plan

The raw BraTS 2020 dataset will be stored inside the repository under:

data/raw/BraTS Adult Glioma (GLI) Training Dataset
(distributed via the BraTS 2023 Synapse project)/

### Intended subfolders

#### 1) original_download/
Purpose:
- store the original downloaded archive/package files obtained from the official BraTS 2020 access route
- keep the untouched source download separate from extracted contents

Path:
- `data/raw/BraTS Adult Glioma (GLI) Training Dataset
(distributed via the BraTS 2023 Synapse project)/original_download/`

#### 2) extracted/
Purpose:
- store the extracted BraTS 2020 training dataset contents
- this folder will later be inspected by the raw-data audit and preprocessing pipeline

Path:
- `data/raw/BraTS Adult Glioma (GLI) Training Dataset
(distributed via the BraTS 2023 Synapse project)/extracted/`

## Raw Data Handling Rules
1. Download BraTS 2020 only from the official approved access route.
2. Place original downloaded archive files inside:
   - `data/raw/BraTS Adult Glioma (GLI) Training Dataset
(distributed via the BraTS 2023 Synapse project)/original_download/`
3. Extract the dataset inside:
   - `data/raw/BraTS Adult Glioma (GLI) Training Dataset
(distributed via the BraTS 2023 Synapse project)/extracted/`
4. Do not manually rename patient folders or MRI files after extraction.
5. Raw data should remain untouched; all later transformations belong in preprocessing outputs, not in the raw dataset folder.

## Phase 3 Intake Goal
Before preprocessing begins, the project should have:
- BraTS 2020 access route confirmed
- raw download location fixed
- extracted dataset location fixed
- expected raw dataset structure ready for inspection