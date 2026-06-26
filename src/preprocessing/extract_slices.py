from pathlib import Path
import nibabel as nib
import numpy as np

DATASET_ROOT = Path(
    "data/raw/brats_gli_2023/extracted/ASNR-MICCAI-BraTS2023-GLI-Challenge-TrainingData"
)


def main():

    patients = sorted([p for p in DATASET_ROOT.iterdir() if p.is_dir()])

    patient = patients[0]

    print("=" * 60)
    print(f"Patient : {patient.name}")
    print("=" * 60)

    mask_path = patient / f"{patient.name}-seg.nii.gz"

    mask = nib.load(str(mask_path)).get_fdata()

    binary_mask = mask > 0

    depth = binary_mask.shape[2]

    positive = [
        i
        for i in range(depth)
        if np.any(binary_mask[:, :, i])
    ]

    first_slice = min(positive)
    last_slice = max(positive)

    start = max(0, first_slice - 2)
    end = min(depth - 1, last_slice + 2)

    retained = end - start + 1

    print(f"Volume depth          : {depth}")
    print(f"Tumor slices          : {len(positive)}")
    print(f"First tumor slice     : {first_slice}")
    print(f"Last tumor slice      : {last_slice}")
    print(f"Retained start slice  : {start}")
    print(f"Retained end slice    : {end}")
    print(f"Retained slice count  : {retained}")


if __name__ == "__main__":
    main()