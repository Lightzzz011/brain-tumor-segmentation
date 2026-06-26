from pathlib import Path
import random
import pandas as pd

from src.config import DATASET_ROOT, PROJECT_ROOT, RANDOM_SEED

# -----------------------------
# Output Folder
# -----------------------------
SPLIT_DIR = PROJECT_ROOT / "data" / "splits"
SPLIT_DIR.mkdir(parents=True, exist_ok=True)

TRAIN_RATIO = 0.70
VAL_RATIO = 0.15
TEST_RATIO = 0.15


def save_csv(patient_ids, filename):
    df = pd.DataFrame({"patient_id": patient_ids})
    df.to_csv(SPLIT_DIR / filename, index=False)


def main():

    random.seed(RANDOM_SEED)

    patients = sorted(
        [
            p.name
            for p in DATASET_ROOT.iterdir()
            if p.is_dir()
        ]
    )

    random.shuffle(patients)

    total = len(patients)

    train_end = int(total * TRAIN_RATIO)
    val_end = train_end + int(total * VAL_RATIO)

    train = patients[:train_end]
    val = patients[train_end:val_end]
    test = patients[val_end:]

    save_csv(train, "train_patients.csv")
    save_csv(val, "val_patients.csv")
    save_csv(test, "test_patients.csv")

    print("=" * 50)
    print(f"Total Patients : {total}")
    print(f"Train          : {len(train)}")
    print(f"Validation     : {len(val)}")
    print(f"Test           : {len(test)}")
    print("=" * 50)

    print("\nSaved files:")
    print(" - train_patients.csv")
    print(" - val_patients.csv")
    print(" - test_patients.csv")


if __name__ == "__main__":
    main()