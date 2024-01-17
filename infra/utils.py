import os
from typing import Generator
import pathlib


def get_file_name_from_path(file_path):
    return os.path.basename(file_path)


def find_first_cond(data, func, **kwargs):
    for val in data:
        if func(val, **kwargs):
            return val

    return None


def is_file(path: str) -> bool:
    return os.path.isfile(path)


def is_directory_exists(path: str) -> bool:
    return os.path.isdir(path)


def get_files(path: str) -> Generator:
    return pathlib.Path(path).iterdir()
