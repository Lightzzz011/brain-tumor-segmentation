from pathlib import Path
import nibabel as nib
import numpy as np

DATASET_ROOT = Path(
    "data/raw/brats_gli_2023/extracted/ASNR-MICCAI-BraTS2023-GLI-Challenge-TrainingData"
)

REPORT_DIR = Path("data/interim")
REPORT_DIR.mkdir(parents=True, exist_ok=True)


def load_volume(path):
    return nib.load(str(path))


def main():
    patients = sorted([p for p in DATASET_ROOT.iterdir() if p.is_dir()])

    if not patients:
        print("No patient folders found.")
        return

    patient = patients[0]

    print("=" * 50)
    print(f"Patient : {patient.name}")
    print("=" * 50)

    files = {
        "T1ce": patient / f"{patient.name}-t1c.nii.gz",
        "T1": patient / f"{patient.name}-t1n.nii.gz",
        "FLAIR": patient / f"{patient.name}-t2f.nii.gz",
        "T2": patient / f"{patient.name}-t2w.nii.gz",
        "SEG": patient / f"{patient.name}-seg.nii.gz",
    }

    images = {}

    for name, path in files.items():
        img = load_volume(path)
        data = img.get_fdata()

        images[name] = (img, data)

        print(f"{name:7} Shape : {data.shape}")

    print()

    reference = images["FLAIR"][1].shape

    aligned = all(
        images[name][1].shape == reference
        for name in images
    )

    print(f"All modalities aligned : {aligned}")

    spacing = images["FLAIR"][0].header.get_zooms()

    print(f"Voxel spacing          : {spacing}")

    labels = np.unique(images["SEG"][1])

    print(f"Mask labels            : {labels}")

    report_path = REPORT_DIR / "patient_inspection_report.txt"

    with open(report_path, "w") as f:
        f.write(f"Patient: {patient.name}\n")
        f.write(f"Shape: {reference}\n")
        f.write(f"Voxel spacing: {spacing}\n")
        f.write(f"Mask labels: {labels.tolist()}\n")
        f.write(f"Aligned: {aligned}\n")

    print()
    print(f"Report saved to: {report_path}")


if __name__ == "__main__":
    main()