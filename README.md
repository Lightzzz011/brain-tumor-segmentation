# Explainable Brain Tumor Segmentation and Quantitative Analysis Using TransUNet and Attention U-Net

My mini project focused on brain tumor segmentation from MRI scans using deep learning, explainability, and quantitative tumor analysis : )

## Current Status
Phase 1 - Project setup in progress.... 

This project aims to build an end-to-end pipeline for **brain tumor segmentation and analysis** using MRI data from the **BraTS dataset**. The system will compare two segmentation models:

- **Attention U-Net**
- **TransUNet**

In addition to segmentation, the project will include:

- **quantitative tumor analysis** (tumor area and estimated volume)
- **explainability / heatmap visualization**
- a **Streamlit-based demo interface** for running inference and visualizing results

---

## Current Implementation Scope

The currently locked core implementation scope is:

- **Task type:** Binary tumor segmentation
- **Training pipeline:** 2D slice-based
- **Input modalities:** FLAIR + T1ce + T2
- **Excluded for initial build:** T1 modality
- **Models:** Attention U-Net and TransUNet
- **Dataset target:** **BraTS Adult Glioma (GLI) Training Dataset distributed via the BraTS 2023 Synapse project Training Dataset**
- **Demo framework:** Streamlit
- **2D sample format:** axial slices, 3-channel input (FLAIR + T1ce + T2), resized to 224 × 224
- **Split strategy:** patient-wise 70 / 15 / 15 train-validation-test split

---

## Planned Pipeline

BraTS MRI dataset  
→ preprocessing and slice extraction  
→ train/validation pipeline  
→ Attention U-Net vs TransUNet comparison  
→ tumor segmentation  
→ quantitative analysis (tumor area and estimated volume)  
→ explainability / heatmap visualization  
→ Streamlit demo app

---

## Repository Structure

```text
explainable-brain-tumor-segmentation/
│
├─ configs/
├─ data/
│  ├─ raw/
│  ├─ interim/
│  ├─ processed/
│  └─ splits/
├─ docs/
├─ environment/
├─ notebooks/
├─ outputs/
└─ src/
   ├─ analysis/
   ├─ app/
   ├─ data/
   ├─ evaluation/
   ├─ explainability/
   ├─ inference/
   ├─ models/
   ├─ training/
   └─ utils/

---

## Binary Segmentation Target

The project uses a **binary whole-tumor segmentation target** derived from the BraTS multiclass labels.

### BraTS to binary mask mapping
- `0 -> background`
- `1 -> tumor`
- `2 -> tumor`
- `4 -> tumor`

In other words, **all non-zero BraTS tumor labels are merged into one foreground class**.  
This means the segmentation target represents the **whole tumor region** rather than only one tumor subcomponent.

---

## 2D Slice Strategy

The project uses an **axial 2D slice-based training pipeline**.

### Input sample format
Each training sample corresponds to **one axial slice from one BraTS patient case**.

- **Input image shape:** `3 x 224 x 224`
- **Input channels:** FLAIR, T1ce, T2
- **Target mask shape:** `1 x 224 x 224`
- **Target mask type:** binary whole-tumor mask

### Slice retention rule
For each patient volume:
- find all axial slices containing tumor pixels in the binary mask
- keep the tumor-containing slice range
- extend that retained range by **2 slices before** the first tumor slice
- extend it by **2 slices after** the last tumor slice

This keeps the tumor region plus a small amount of surrounding context, while discarding far-away empty slices.

---

## Data Split Strategy

The project uses a **patient-wise** data split to avoid leakage between training and evaluation.

### Split design
- **70%** training patients
- **15%** validation patients
- **15%** test patients

### Important rule
All slices from the same BraTS patient case must remain in the **same split**.  
No patient is allowed to appear across multiple splits.

---

