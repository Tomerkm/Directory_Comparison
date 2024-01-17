import os

FOLDER_FILES_TO_CMP_NAME = "files_to_cmp"
FOLDER_FILES_TYPE_TEXT_NAME = "files_type_text"
FOLDER_FILES_TYPE_TEXT_NAME_2 = "files_type_text_2"
FOLDER_FILES_TYPE_PDF_NAME = "files_type_pdf"
FOLDER_FILES_TYPE_PDF_NAME_2 = "files_type_pdf_2"

CURR_FOLDER_PATH = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE_NAME = os.path.join(CURR_FOLDER_PATH, "config.ini")

FOLDERS_FILES_PATH = os.path.join(CURR_FOLDER_PATH, FOLDER_FILES_TO_CMP_NAME)

FOLDER_FILES_TYPE_TEXT_PATH = os.path.join(FOLDERS_FILES_PATH, FOLDER_FILES_TYPE_TEXT_NAME)
FOLDER_FILES_TYPE_TEXT_2_PATH = os.path.join(FOLDERS_FILES_PATH, FOLDER_FILES_TYPE_TEXT_NAME_2)
FOLDER_FILES_TYPE_PDF_PATH = os.path.join(FOLDERS_FILES_PATH, FOLDER_FILES_TYPE_PDF_NAME)
FOLDER_FILES_TYPE_PDF_2_PATH = os.path.join(FOLDERS_FILES_PATH, FOLDER_FILES_TYPE_PDF_NAME_2)

# FORMAT CHECKING FILE NAMES:
# <path file a>: str, <path file b>: str, <expected result>: List[str]

# <START>

TEST_DATA_PATH_TXT_DIFF = [
    (FOLDER_FILES_TYPE_TEXT_PATH, FOLDER_FILES_TYPE_TEXT_2_PATH, ["upperCaseLatin_and_digits.txt"]),
    (FOLDER_FILES_TYPE_TEXT_2_PATH, FOLDER_FILES_TYPE_TEXT_PATH, ["mixedLatin.txt"])
]

TEST_DATA_PATH_PDF_DIFF = [
    (FOLDER_FILES_TYPE_PDF_PATH, FOLDER_FILES_TYPE_PDF_2_PATH, ["File-3jS2W.pdf", "File-CIQri.pdf"]),
    (FOLDER_FILES_TYPE_PDF_2_PATH, FOLDER_FILES_TYPE_PDF_PATH, ["File-EW3U7.pdf", "File-QBU1q.pdf"])
]

TEST_DATA_PDF_AND_TXT_DIFF = [
    (FOLDER_FILES_TYPE_TEXT_PATH, FOLDER_FILES_TYPE_PDF_PATH, ["all_Latin_Letters_And_Digits.txt", "digits.txt", "lower_case_latin.txt", "upperCaseLatin_and_digits.txt"]),
    (FOLDER_FILES_TYPE_PDF_PATH, FOLDER_FILES_TYPE_TEXT_PATH, ["File-3jS2W.pdf", "File-4N73H.pdf", "File-CIQri.pdf"])
]

TEST_DATA_PATH_TXT_COMMON = [
    (FOLDER_FILES_TYPE_TEXT_PATH, FOLDER_FILES_TYPE_TEXT_2_PATH, ["all_Latin_Letters_And_Digits.txt", "digits.txt", "lower_case_latin.txt"])
]

TEST_DATA_PATH_PDF_COMMON = [
    (FOLDER_FILES_TYPE_PDF_PATH, FOLDER_FILES_TYPE_PDF_2_PATH, ["File-4N73H.pdf"])
]

# <END>

