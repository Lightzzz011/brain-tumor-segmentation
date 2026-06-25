# Environment Setup Notes

This folder stores environment and installation notes for the project...

Planned items:
- Python version used
- virtual environment setup steps
- PyTorch installation details
- CUDA/GPU verification notes
- package installation troubleshooting

## Project Environment
- Virtual environment name: `.venv`
- Python version used: `3.10.11`
- Environment created inside project root

## Activation Command (CMD)
```cmd
.venv\Scripts\activate


## Base Packages Installed
The following non-PyTorch packages were installed in the project virtual environment:

- numpy
- pandas
- matplotlib
- opencv-python
- nibabel
- scikit-learn
- tqdm
- pyyaml
- jupyter

## Base Environment Check
A basic import verification script is available at:

`src/utils/system_check.py`

## Deep Learning Stack
Installed deep learning packages:
- torch
- torchvision
- torchaudio

PyTorch was installed using the official CUDA wheel index for GPU-enabled training.

## Environment Validation Script
Current environment verification script:
`src/utils/system_check.py`

This script checks:
- base package imports
- PyTorch import
- CUDA availability
- GPU name
- a small tensor operation on GPU

## PyTorch GPU Compatibility Note
Initial installation using CUDA 11.8 wheels produced an `sm_120` compatibility warning for the NVIDIA GeForce RTX 5050 Laptop GPU.

The environment was corrected by reinstalling PyTorch with the CUDA 12.8 wheel index for RTX 50-series GPU compatibility.