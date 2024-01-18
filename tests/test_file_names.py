import pytest

from definitions import TEST_DATA_PATH_TXT_DIFF, TEST_DATA_PATH_PDF_DIFF, TEST_DATA_PDF_AND_TXT_DIFF, \
    TEST_DATA_PATH_TXT_COMMON, TEST_DATA_PATH_PDF_COMMON
from logic.set_diff_and_common_names import set_diff_names_two_folders, common_names_two_folders


@pytest.mark.parametrize("path_files_a, path_files_b, expected_res", TEST_DATA_PATH_TXT_DIFF,
                         ids=["files text type in folder a but not in b", "files text type in folder b but not in a"])
def test_cmp_txt_files_name(path_files_a, path_files_b, expected_res, get_test_name, get_logger, get_config):
    res = set_diff_names_two_folders(path_files_a, path_files_b, logger=get_logger)
    assert len(res)
    for file_name in res:
        assert file_name in expected_res


@pytest.mark.parametrize("path_files_a, path_files_b, expected_res", TEST_DATA_PATH_PDF_DIFF,
                         ids=["files pdf type in folder a but not in b", "files pdf type in folder b but not in a"])
def test_cmp_pdf_files_name(path_files_a, path_files_b, expected_res, get_test_name, get_logger, get_config):
    res = set_diff_names_two_folders(path_files_a, path_files_b, logger=get_logger)
    assert len(res)
    for file_name in res:
        assert file_name in expected_res


@pytest.mark.parametrize("path_files_a, path_files_b, expected_res", TEST_DATA_PDF_AND_TXT_DIFF,
                         ids=["files in folder a but not in b", "files in folder b but not in a"])
def test_cmp_diff_type_files_name(path_files_a, path_files_b, expected_res, get_test_name, get_logger, get_config):
    res = set_diff_names_two_folders(path_files_a, path_files_b, logger=get_logger)
    assert len(res)
    for file_name in res:
        assert file_name in expected_res


@pytest.mark.parametrize("path_files_a, path_files_b, expected_res", TEST_DATA_PATH_TXT_COMMON,
                         ids=["common files names text type"])
def test_common_names_type_text(path_files_a, path_files_b, expected_res, get_test_name, get_logger, get_config):
    res = common_names_two_folders(path_files_a, path_files_b, logger=get_logger)
    assert len(res)
    for file_name in res:
        assert file_name in expected_res


@pytest.mark.parametrize("path_files_a, path_files_b, expected_res", TEST_DATA_PATH_PDF_COMMON,
                         ids=["common files names pdf type"])
def test_common_names_type_pdf(path_files_a, path_files_b, expected_res, get_test_name, get_logger, get_config):
    res = common_names_two_folders(path_files_a, path_files_b, logger=get_logger)
    assert len(res)
    for file_name in res:
        assert file_name in expected_res
