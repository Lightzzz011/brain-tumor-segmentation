from src.dataset.cache import PatientCache

cache = PatientCache()

patient = cache.get("BraTS-GLI-00000-000")

print(patient["patient_id"])
print(patient["flair"].shape)
print(patient["t1ce"].shape)
print(patient["t2"].shape)
print(patient["seg"].shape)