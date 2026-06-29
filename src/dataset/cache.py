from collections import OrderedDict

from src.config import DATASET_ROOT
from src.preprocessing.io_utils import load_patient


class PatientCache:
    def __init__(self, max_size=8):
        self.max_size = max_size
        self.cache = OrderedDict()

    def get(self, patient_id):

        if patient_id in self.cache:
            self.cache.move_to_end(patient_id)
            return self.cache[patient_id]

        patient_dir = DATASET_ROOT / patient_id

        data = load_patient(patient_dir)

        self.cache[patient_id] = data

        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)

        return data