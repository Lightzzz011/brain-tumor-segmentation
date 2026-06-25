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
- **Dataset target:** BraTS 2020 or BraTS 2021
- **Demo framework:** Streamlit

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