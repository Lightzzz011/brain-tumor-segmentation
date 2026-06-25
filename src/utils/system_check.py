def main():
    print("Running base environment import check...")

    import numpy as np
    import pandas as pd
    import matplotlib
    import cv2
    import nibabel as nib
    import sklearn
    import yaml
    import tqdm

    print("All base imports succeeded.")
    print(f"NumPy version: {np.__version__}")
    print(f"Pandas version: {pd.__version__}")
    print(f"Matplotlib version: {matplotlib.__version__}")
    print(f"OpenCV version: {cv2.__version__}")
    print(f"NiBabel version: {nib.__version__}")
    print(f"scikit-learn version: {sklearn.__version__}")
    print(f"PyYAML version: {yaml.__version__}")


if __name__ == '__main__':
    main()