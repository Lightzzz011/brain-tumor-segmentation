from src.dataset.brain_tumor_dataset import BrainTumorDataset

dataset = BrainTumorDataset("train")

print("Dataset length:", len(dataset))

for i in range(20):

    image, mask = dataset[i]

    print(
        i,
        image.shape,
        mask.shape,
        mask.unique().tolist()
    )

    if len(mask.unique()) > 1:
        print(f"\nFirst tumor slice found at dataset index: {i}")
        break