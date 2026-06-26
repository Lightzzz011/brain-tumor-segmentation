from pathlib import Path
import pandas as pd

# -----------------------------
# Dataset Root
# -----------------------------
DATASET_ROOT = Path(
    "data/raw/brats_gli_2023/extracted/ASNR-MICCAI-BraTS2023-GLI-Challenge-TrainingData"
)

OUTPUT_DIR = Path("data/interim")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

REQUIRED_SUFFIXES = [
    "-t1c.nii.gz",
    "-t1n.nii.gz",
    "-t2f.nii.gz",
    "-t2w.nii.gz",
    "-seg.nii.gz",
]


def main():
    patient_dirs = sorted([p for p in DATASET_ROOT.iterdir() if p.is_dir()])

    print(f"Patients found: {len(patient_dirs)}")

    records = []

    for patient in patient_dirs:
        files = [f.name for f in patient.iterdir() if f.is_file()]

        status = {}

        for suffix in REQUIRED_SUFFIXES:
            status[suffix] = any(f.endswith(suffix) for f in files)

        records.append(
            {
                "patient_id": patient.name,
                **status,
                "complete": all(status.values()),
            }
        )

    df = pd.DataFrame(records)

    output_csv = OUTPUT_DIR / "dataset_audit.csv"
    df.to_csv(output_csv, index=False)

    complete = df["complete"].sum()
    incomplete = len(df) - complete

    print("-" * 40)
    print(f"Complete patients   : {complete}")
    print(f"Incomplete patients : {incomplete}")
    print(f"CSV saved to        : {output_csv}")


if __name__ == "__main__":
    main()