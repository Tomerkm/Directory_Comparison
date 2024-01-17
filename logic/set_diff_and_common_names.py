from typing import Generator, List

from infra.utils import get_files, is_file, is_directory_exists


def get_files_names(files: Generator) -> Generator:
    for file_path in files:
        if is_file(file_path):
            yield file_path.name


def check_directory_paths(paths: List[str], logger):
    for path in paths:
        if not is_directory_exists(path):
            errorMsg = f"\n Folder Error: the path {path} do not appear \n"
            logger.error(errorMsg)
            raise Exception(errorMsg)


def get_file_names_of_two_folders(path_files_a: str, path_files_b: str, logger):
    logger.info(f"\n Folder A path: {path_files_a} \n")
    logger.info(f"\n Folder B path: {path_files_b} \n")

    check_directory_paths(paths=[path_files_a, path_files_b], logger=logger)

    files_names_a = set(get_files_names(get_files(path_files_a)))
    files_names_b = set(get_files_names(get_files(path_files_b)))

    logger.info(f"\n files names of parameter folder A {files_names_a} \n")
    logger.info(f"\n files names of parameter folder B {files_names_b} \n")

    return files_names_a, files_names_b


def set_diff_names_two_folders(path_files_a: str, path_files_b: str, logger):
    files_names_a, files_names_b = get_file_names_of_two_folders(path_files_a, path_files_b, logger)
    res = files_names_a - files_names_b
    logger.info(f"\n files names in parameter folder A but not in folder B {res} \n")

    return res


def common_names_two_folders(path_files_a: str, path_files_b: str, logger):
    files_names_a, files_names_b = get_file_names_of_two_folders(path_files_a, path_files_b, logger)
    res = files_names_a & files_names_b
    logger.info(f"\n common files names found in both folders A and B {res} \n")

    return res


