from pathlib import Path

import nibabel as nib
import numpy as np
import pandas as pd

DATASET_ROOT = Path(
    "data/raw/brats_gli_2023/extracted/ASNR-MICCAI-BraTS2023-GLI-Challenge-TrainingData"
)

OUTPUT_ROOT = Path("data/processed/sample_patient")
IMAGE_DIR = OUTPUT_ROOT / "images"
MASK_DIR = OUTPUT_ROOT / "masks"

IMAGE_DIR.mkdir(parents=True, exist_ok=True)
MASK_DIR.mkdir(parents=True, exist_ok=True)


def load(path):
    return nib.load(str(path)).get_fdata()


def main():

    patient = sorted([p for p in DATASET_ROOT.iterdir() if p.is_dir()])[0]

    print(f"Processing {patient.name}")

    flair = load(patient / f"{patient.name}-t2f.nii.gz")
    t1ce = load(patient / f"{patient.name}-t1c.nii.gz")
    t2 = load(patient / f"{patient.name}-t2w.nii.gz")
    seg = load(patient / f"{patient.name}-seg.nii.gz")

    binary = (seg > 0).astype(np.uint8)

    positive = [
        i for i in range(binary.shape[2])
        if np.any(binary[:, :, i])
    ]

    start = max(0, min(positive) - 2)
    end = min(binary.shape[2] - 1, max(positive) + 2)

    metadata = []

    for idx in range(start, end + 1):

        image = np.stack([
            flair[:, :, idx],
            t1ce[:, :, idx],
            t2[:, :, idx]
        ], axis=-1).astype(np.float32)

        mask = binary[:, :, idx]

        np.save(IMAGE_DIR / f"{idx:03d}.npy", image)
        np.save(MASK_DIR / f"{idx:03d}.npy", mask)

        metadata.append({
            "patient_id": patient.name,
            "slice_index": idx,
            "has_tumor": bool(np.any(mask))
        })

    pd.DataFrame(metadata).to_csv(
        OUTPUT_ROOT / "metadata.csv",
        index=False
    )

    print(f"Saved {len(metadata)} slices.")
    print("Done.")


if __name__ == "__main__":
    main()