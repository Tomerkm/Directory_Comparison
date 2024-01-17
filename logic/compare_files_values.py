import os
from datetime import datetime
import zipfile
from definitions import OUTPUT_RESULT_PDF
from infra.utils import get_files, find_first_cond, get_file_name_from_path
from logic.set_diff_and_common_names import common_names_two_folders
import aspose.words as aw


def get_common_files_path(path_files_a: str, path_files_b: str, logger):
    common_file_names = common_names_two_folders(path_files_a, path_files_b, logger=logger)

    func_call = lambda full_path, file_name: str(full_path).endswith(file_name)
    common_full_path_a = []
    common_full_path_b = []

    for file_name in common_file_names:
        logger.info(f"\n\n searching for file name {file_name} \n\n")

        files_names_a = get_files(path_files_a)
        files_names_b = get_files(path_files_b)

        common_full_path_a.append(str(find_first_cond(data=files_names_a, func=func_call, file_name=file_name)))
        common_full_path_b.append(str(find_first_cond(data=files_names_b, func=func_call, file_name=file_name)))

    return common_full_path_a, common_full_path_b


def print_diff_on_files(file_a, file_b, logger):
    file_1_line = file_a.readline()
    file_2_line = file_b.readline()
    line_no = 1
    cnt_diff = 0

    # Compare the lines from both file
    if file_1_line != file_2_line:
        cnt_diff += 1

        # otherwise output the line on file1 and use @ sign
        if file_1_line == '':
            logger.info(f"\n\n@, Line-{line_no} {file_1_line}\n\n")
        else:
            logger.info(f"\n\n@-, Line-{line_no} {file_1_line}\n\n")

        # otherwise output the line on file2 and use # sign
        if file_2_line == '':
            logger.info(f"\n\n#, Line-{line_no} {file_2_line}\n\n")
        else:
            logger.info(f"\n\n#+ Line-{line_no} {file_2_line}\n\n")

        # Read the next line from the file
        file_1_line = file_a.readline()
        file_2_line = file_b.readline()

    line_no += 1
    return cnt_diff


def compare_file_txt_values(path_files_a: str, path_files_b: str, logger):
    common_full_path_a, common_full_path_b = get_common_files_path(path_files_a, path_files_b, logger=logger)

    # same size
    size = len(common_full_path_a)
    logger.info(f"\n\n number of same file name: {size} \n\n")
    list_cnt_res = []

    for i in range(0, size):
        with open(common_full_path_a[i], 'r') as fp_a, open(common_full_path_b[i], 'r') as fp_b:
            logger.debug(f"\n\n comparing files: {common_full_path_a[i]} and {common_full_path_b[i]} \n\n")
            cnt_res = print_diff_on_files(fp_a, fp_b, logger)

            logger.debug(f"\n\n cnt diff: {cnt_res}  \n\n")
            list_cnt_res.append(cnt_res)

    return list_cnt_res


def compare_file_pdf_values(path_files_a: str, path_files_b: str, logger):
    common_full_path_a, common_full_path_b = get_common_files_path(path_files_a, path_files_b, logger=logger)

    # same size
    size = len(common_full_path_a)
    logger.info(f"\n\n number of same file name: {size} \n\n")

    for i in range(0, size):
        logger.debug(f"\n\n comparing files: {common_full_path_a[i]} and {common_full_path_b[i]} \n\n")
        file_name = get_file_name_from_path(common_full_path_a[i])
        docA = aw.Document(common_full_path_a[i])
        docB = aw.Document(common_full_path_b[i])

        # There should be no revisions before comparison.
        docA.accept_all_revisions()
        docB.accept_all_revisions()

        docA.compare(docB, "Author Name", datetime.now())
        docA.save(f"{os.path.join(OUTPUT_RESULT_PDF, str(datetime.now().date()))} - {file_name}")


def compare_zip_files_sizes(path_files_a: str, path_files_b: str, logger):
    common_full_path_a, common_full_path_b = get_common_files_path(path_files_a, path_files_b, logger=logger)

    # same size
    size = len(common_full_path_a)
    logger.info(f"\n\n number of same file name: {size} \n\n")
    is_at_least_one_diff = False

    for i in range(0, size):
        logger.info(f"\n\n comparing files sizes: {common_full_path_a[i]} and {common_full_path_b[i]} \n\n")
        zp_a = zipfile.ZipFile(common_full_path_a[i])
        zp_b = zipfile.ZipFile(common_full_path_b[i])

        size_a = sum([zinfo.file_size for zinfo in zp_a.filelist])
        size_b = sum([zinfo.file_size for zinfo in zp_b.filelist])
        zip_kb_a = float(size_a) / 1000  # kB
        zip_kb_b = float(size_b) / 1000  # kB

        if size_a != size_b:
            is_at_least_one_diff = True

        logger.info(f"\n\n file size in param a = {zip_kb_a} kb \n\n")
        logger.info(f"\n\n file size in param b = {zip_kb_b} kb \n\n")


    return is_at_least_one_diff