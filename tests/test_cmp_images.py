import pytest

from definitions import DATA_FILES_IMG_CMP
from logic.compare_images_values import compare_img_files


@pytest.mark.parametrize("path_files_a, path_files_b", DATA_FILES_IMG_CMP,
                         ids=["compare images"])
def test_cmp_txt_files_values(path_files_a, path_files_b, get_test_name, get_logger, get_config):
    compare_img_files(path_files_a, path_files_b, logger=get_logger)
