import pytest

from definitions import DATA_FILES_TXT_CMP, FOLDER_FILES_TYPE_TEXT_PATH, DATA_FILES_PDF_CMP, DATA_FILES_ZIP_CMP_SIZE
from logic.compare_files_values import compare_file_txt_values, compare_file_pdf_values, compare_zip_files_sizes


@pytest.mark.parametrize("path_files_a, path_files_b", DATA_FILES_TXT_CMP,
                         ids=["compare text files"])
def test_cmp_txt_files_values(path_files_a, path_files_b, get_test_name, get_logger, get_config):
    res = compare_file_txt_values(path_files_a, path_files_b, logger=get_logger)
    for num in res:
        assert 0 < num


def test_cmp_same_txt_files_values(get_test_name, get_logger, get_config):
    res = compare_file_txt_values(FOLDER_FILES_TYPE_TEXT_PATH, FOLDER_FILES_TYPE_TEXT_PATH, logger=get_logger)
    for num in res:
        assert 0 == num


@pytest.mark.parametrize("path_files_a, path_files_b", DATA_FILES_PDF_CMP,
                         ids=["compare pdf files"])
def test_cmp_pdf_files_values(path_files_a, path_files_b, get_test_name, get_logger, get_config):
    compare_file_pdf_values(path_files_a, path_files_b, logger=get_logger)


@pytest.mark.parametrize("path_files_a, path_files_b", DATA_FILES_ZIP_CMP_SIZE,
                         ids=["compare zip files sizes"])
def test_cmp_zip_files_values(path_files_a, path_files_b, get_test_name, get_logger, get_config):
    assert compare_zip_files_sizes(path_files_a, path_files_b, logger=get_logger) == True