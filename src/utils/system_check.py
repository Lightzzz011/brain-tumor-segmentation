def main():
    print("=== Base Package Import Check ===")

    import numpy as np
    import pandas as pd
    import matplotlib
    import cv2
    import nibabel as nib
    import sklearn
    import yaml
    import tqdm
    import torch

    print("All imports succeeded.")
    print()

    print("=== Package Versions ===")
    print(f"NumPy version: {np.__version__}")
    print(f"Pandas version: {pd.__version__}")
    print(f"Matplotlib version: {matplotlib.__version__}")
    print(f"OpenCV version: {cv2.__version__}")
    print(f"NiBabel version: {nib.__version__}")
    print(f"scikit-learn version: {sklearn.__version__}")
    print(f"PyYAML version: {yaml.__version__}")
    print(f"PyTorch version: {torch.__version__}")
    print()

    print("=== PyTorch / CUDA Check ===")
    cuda_available = torch.cuda.is_available()
    print(f"CUDA available: {cuda_available}")

    if cuda_available:
        device_count = torch.cuda.device_count()
        current_device = torch.cuda.current_device()
        gpu_name = torch.cuda.get_device_name(current_device)

        print(f"CUDA device count: {device_count}")
        print(f"Current CUDA device index: {current_device}")
        print(f"Current GPU name: {gpu_name}")

        if torch.version.cuda is not None:
            print(f"PyTorch CUDA runtime version: {torch.version.cuda}")
        else:
            print("PyTorch CUDA runtime version: None")

        # Tiny GPU tensor test
        x = torch.rand((2, 3), device="cuda")
        y = torch.rand((2, 3), device="cuda")
        z = x + y

        print()
        print("=== GPU Tensor Test ===")
        print("Successfully created and added tensors on GPU.")
        print("Result tensor:")
        print(z)
    else:
        print("WARNING: CUDA is not available. PyTorch is currently running on CPU only.")

    print()
    print("System check completed.")


if __name__ == "__main__":
    main()