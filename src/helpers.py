import os
from collections import defaultdict
from pathlib import Path
from typing import Any


def get_full_file_path(file_path: str) -> str:
    path_to_root = Path(__file__).parent.parent
    path_to_dataset = os.path.join(path_to_root, file_path)
    return path_to_dataset


def sort_data_by_key(
    data: list[dict[str, Any]], key: str, reverse: bool = False
) -> None:
    data.sort(key=lambda x: x[key], reverse=reverse)


def group_by_key(records: list[dict[str, Any]], key: Any) -> dict[str, int]:
    result: defaultdict[Any, int] = defaultdict(int)
    for record in records:
        result[record[key]] += 1
    return result
