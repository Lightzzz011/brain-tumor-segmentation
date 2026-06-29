import cv2
import numpy as np
import torch
from torch.utils.data import Dataset

from src.dataset.cache import PatientCache
from src.dataset.slice_index import build_slice_index
from src.config import MODEL_IMAGE_SIZE


class BrainTumorDataset(Dataset):

    def __init__(self, split="train"):

        self.index = build_slice_index(split)
        self.cache = PatientCache()

        print(f"{split.capitalize()} slices: {len(self.index)}")

    def __len__(self):
        return len(self.index)

    def __getitem__(self, idx):

        patient_id, slice_idx = self.index[idx]

        patient = self.cache.get(patient_id)

        image = np.stack(
            [
                patient["flair"][:, :, slice_idx],
                patient["t1ce"][:, :, slice_idx],
                patient["t2"][:, :, slice_idx],
            ],
            axis=-1,
        )

        mask = (patient["seg"][:, :, slice_idx] > 0).astype(np.float32)

        image = cv2.resize(
            image,
            (MODEL_IMAGE_SIZE, MODEL_IMAGE_SIZE),
            interpolation=cv2.INTER_LINEAR,
        )

        mask = cv2.resize(
            mask,
            (MODEL_IMAGE_SIZE, MODEL_IMAGE_SIZE),
            interpolation=cv2.INTER_NEAREST,
        )

        image = image.astype(np.float32)

        image = (image - image.mean()) / (image.std() + 1e-8)

        image = torch.from_numpy(image).permute(2, 0, 1)

        mask = torch.from_numpy(mask).unsqueeze(0)

        return image, mask