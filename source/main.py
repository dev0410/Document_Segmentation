import cv2
import argparse
from segment import *
from transform import *


def image_process(image_path, result_path):
    """
    ### description
    segment and transform document from the image

    ### parameters
    image_path: original image path
    result_path: result image path
    """
    # read image
    img = cv2.imread(image_path)
    # show_img(img)

    # padding images
    img = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_WRAP)

    # get contour of document
    contour = get_contour(img)

    # remove background of image
    img = remove_background(img, contour)
    # show_img(img)

    # get shape information of document
    size, center, angle, w, h = get_shape(contour)

    # get sub region of image
    img = cv2.getRectSubPix(img, (size, size), center)
    # show_img(img)

    # rotate image
    img = rotate_img(img, (size / 2, size / 2), angle, w, h)
    # show_img(img)


if __name__ == '__main__':
    # set argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='path of original image')
    parser.add_argument('--output', type=str, help='path of result image')
    args = parser.parse_args()

    # process image
    image_process(args.input, args.output)
