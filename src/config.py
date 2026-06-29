from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Dataset
DATASET_ROOT = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "brats_gli_2023"
    / "extracted"
    / "ASNR-MICCAI-BraTS2023-GLI-Challenge-TrainingData"
)

# Processed Dataset
PROCESSED_ROOT = PROJECT_ROOT / "data" / "processed"

PATIENT_OUTPUT_DIR = PROCESSED_ROOT / "patients"

# Other folders

INTERIM_DIR = PROJECT_ROOT / "data" / "interim"

FIGURE_DIR = PROJECT_ROOT / "outputs" / "figures"

# Model Input
MODEL_IMAGE_SIZE = 224

# Random Seed
RANDOM_SEED = 42