from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image, ImageChops
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
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)

    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    # show first image
    fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")

    # show the second image
    fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")

    # show the images
    plt.show()


def compare_giff_images(imageA, imageB):
    # assign images
    img1 = Image.open(imageA)
    img2 = Image.open(imageB)

    # finding difference
    diff = ImageChops.difference(img1, img2)

    # showing the difference
    diff.show()


def compare_img_files(path_files_a: str, path_files_b: str, logger):
    common_full_path_a, common_full_path_b = get_common_files_path(path_files_a, path_files_b, logger=logger)

    # same size
    size = len(common_full_path_a)
    logger.info(f"\n\n number of same images name: {size} \n\n")

    for i in range(0, size):
        file_name = get_file_name_from_path(common_full_path_a[i])
        if file_name.endswith(".jpg"):
            image_val_a = cv2.imread(common_full_path_a[i])
            image_val_b = cv2.imread(common_full_path_b[i])

            image_val_a = cv2.cvtColor(image_val_a, cv2.COLOR_BGR2GRAY)
            image_val_b = cv2.cvtColor(image_val_b, cv2.COLOR_BGR2GRAY)

            compare_images(image_val_a, image_val_b, title=f"image name compare: {file_name}")

        else:
            compare_giff_images(common_full_path_a[i], common_full_path_b[i])