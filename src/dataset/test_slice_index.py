from src.dataset.slice_index import build_slice_index

index = build_slice_index("train")

print("Total retained slices:", len(index))
print()

print(index[:10])