from pathlib import Path

import matplotlib.pyplot as plt
import nibabel as nib

# -------------------------------------------------
# Dataset Root
# -------------------------------------------------
DATASET_ROOT = Path(
    "data/raw/brats_gli_2023/extracted/ASNR-MICCAI-BraTS2023-GLI-Challenge-TrainingData"
)

OUTPUT_DIR = Path("outputs/figures")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_volume(path):
    return nib.load(str(path)).get_fdata()


def main():

    patients = sorted([p for p in DATASET_ROOT.iterdir() if p.is_dir()])

    patient = patients[0]

    flair = load_volume(patient / f"{patient.name}-t2f.nii.gz")
    t1ce = load_volume(patient / f"{patient.name}-t1c.nii.gz")
    t2 = load_volume(patient / f"{patient.name}-t2w.nii.gz")
    mask = load_volume(patient / f"{patient.name}-seg.nii.gz")

    # Middle axial slice
    slice_idx = flair.shape[2] // 2

    fig, axes = plt.subplots(1, 4, figsize=(16, 4))

    images = [
        (flair[:, :, slice_idx], "FLAIR"),
        (t1ce[:, :, slice_idx], "T1ce"),
        (t2[:, :, slice_idx], "T2"),
        (mask[:, :, slice_idx], "Mask"),
    ]

    for ax, (img, title) in zip(axes, images):
        ax.imshow(img.T, cmap="gray", origin="lower")
        ax.set_title(title)
        ax.axis("off")

    plt.tight_layout()

    output_file = OUTPUT_DIR / "patient_visualization.png"

    plt.savefig(output_file, dpi=200)
    plt.close()

    print(f"Figure saved to: {output_file}")


if __name__ == "__main__":
    main()