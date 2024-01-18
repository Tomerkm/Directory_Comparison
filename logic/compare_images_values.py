from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
from infra.utils import get_files, find_first_cond, get_file_name_from_path
from logic.set_diff_and_common_names import common_names_two_folders


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


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB, title):

    ROW_SIZE = 4
    COL_SIZE = 1

    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)

    diff_a_b = cv2.subtract(imageA, imageB)
    diff_b_a = cv2.subtract(imageB, imageA)

    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    # show first image
    fig.add_subplot(ROW_SIZE, COL_SIZE, 1)
    plt.title("imageA")
    plt.imshow(imageA)
    plt.axis("off")

    # show the second image
    fig.add_subplot(ROW_SIZE, COL_SIZE, 2)
    plt.title("imageB")
    plt.imshow(imageB)
    plt.axis("off")

    # show the third diff image
    fig.add_subplot(ROW_SIZE, COL_SIZE, 3)
    plt.title("imageA - ImageB")
    plt.imshow(diff_a_b)
    plt.axis("off")

    # show the forth diff image
    fig.add_subplot(ROW_SIZE, COL_SIZE, 4)
    plt.title("imageB - ImageA")
    plt.imshow(diff_b_a)
    plt.axis("off")

    # show the images
    plt.show()


def compare_img_files(path_files_a: str, path_files_b: str, logger):
    common_full_path_a, common_full_path_b = get_common_files_path(path_files_a, path_files_b, logger=logger)

    # same size
    size = len(common_full_path_a)
    logger.info(f"\n\n number of same images name: {size} \n\n")

    for i in range(0, size):
        file_name = get_file_name_from_path(common_full_path_a[i])
        image_val_a = cv2.imread(common_full_path_a[i])
        image_val_b = cv2.imread(common_full_path_b[i])

        image_val_a = cv2.cvtColor(image_val_a, cv2.COLOR_BGR2GRAY)
        image_val_b = cv2.cvtColor(image_val_b, cv2.COLOR_BGR2GRAY)

        compare_images(image_val_a, image_val_b, title=f"image name compare: {file_name}")
