import os
from pathlib import Path


def get_full_file_path(file_path: str) -> str:
    path_to_root = Path(__file__).parent.parent
    path_to_dataset = os.path.join(path_to_root, file_path)
    return path_to_dataset


