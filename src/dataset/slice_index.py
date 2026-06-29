from pathlib import Path

import nibabel as nib
import numpy as np
import pandas as pd

from src.config import DATASET_ROOT, PROJECT_ROOT


def build_slice_index(split: str):
    split_file = (
        PROJECT_ROOT
        / "data"
        / "splits"
        / f"{split}_patients.csv"
    )

    patient_ids = pd.read_csv(split_file)["patient_id"].tolist()

    index = []

    for patient_id in patient_ids:

        patient_dir = DATASET_ROOT / patient_id

        seg_path = patient_dir / f"{patient_id}-seg.nii.gz"

        mask = nib.load(str(seg_path)).get_fdata()

        binary = mask > 0

        positive = [
            i
            for i in range(binary.shape[2])
            if np.any(binary[:, :, i])
        ]

        if not positive:
            continue

        start = max(0, min(positive) - 2)
        end = min(binary.shape[2] - 1, max(positive) + 2)

        for slice_idx in range(start, end + 1):
            index.append((patient_id, slice_idx))

    return index