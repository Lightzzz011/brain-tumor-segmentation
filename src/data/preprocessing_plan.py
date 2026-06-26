from pathlib import Path
import nibabel as nib
import numpy as np
import pandas as pd

DATASET_ROOT = Path(
    "data/raw/brats_gli_2023/extracted/ASNR-MICCAI-BraTS2023-GLI-Challenge-TrainingData"
)

OUTPUT_DIR = Path("data/interim")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():

    patients = sorted([p for p in DATASET_ROOT.iterdir() if p.is_dir()])

    records = []

    total_original = 0
    total_retained = 0
    total_positive = 0

    for patient in patients:

        mask_path = patient / f"{patient.name}-seg.nii.gz"

        mask = nib.load(str(mask_path)).get_fdata()

        binary = mask > 0

        depth = binary.shape[2]

        positive = [
            i
            for i in range(depth)
            if np.any(binary[:, :, i])
        ]

        total_original += depth

        if len(positive) == 0:
            continue

        first_idx = min(positive)
        last_idx = max(positive)

        start = max(0, first_idx - 2)
        end = min(depth - 1, last_idx + 2)

        retained = end - start + 1

        total_positive += len(positive)
        total_retained += retained

        records.append(
            {
                "patient_id": patient.name,
                "depth": depth,
                "positive_slices": len(positive),
                "first_positive": first_idx,
                "last_positive": last_idx,
                "retained_slices": retained,
            }
        )

    df = pd.DataFrame(records)

    output_csv = OUTPUT_DIR / "slice_statistics.csv"
    df.to_csv(output_csv, index=False)

    print("=" * 50)
    print(f"Patients analysed      : {len(df)}")
    print(f"Original slices        : {total_original}")
    print(f"Tumor-positive slices  : {total_positive}")
    print(f"Retained slices        : {total_retained}")
    print("=" * 50)

    print(f"\nSaved: {output_csv}")


if __name__ == "__main__":
    main()