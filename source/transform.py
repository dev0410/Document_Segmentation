import cv2
import numpy as np


def get_shape(contour):
    """
    ### description
    get position, size and angle of document

    ### parameters
    contour: region of document

    ### return values
    size: size of document region
    pos: center position of document
    angle: angle of document
    w: width of document
    h: height of document
    """
    # find minarea rectangle
    rect = cv2.minAreaRect(contour)
    box = np.int0(cv2.boxPoints(rect))

	# get width, height and angle of document
    W = int(rect[1][0])
    H = int(rect[1][1])
    angle = rect[2]

	# make wide rectangle
    if W < H:
        W, H = H, W
        angle -= 90

	# set crop rectangle
    x1 = min(box[:, 0])
    x2 = max(box[:, 0])
    y1 = min(box[:, 1])
    y2 = max(box[:, 1])

	# set crop rectangle
    size = int(max((x2 - x1), (y2 - y1)))

    return size, ((x1 + x2) / 2, (y1 + y2) / 2), angle, W, H


def rotate_img(img, center, angle, w, h):
    """
    ### description
    rotate image with angle

    ### parameters
    img: original image
    center: center pos of img
    angle: rotatino angle
    w: width of image
    h: height of image

    ### return values
    image: rotated image
    """
    # make rotation matrix
    rotate_mat = cv2.getRotationMatrix2D(center, angle, 1.0)

    # rotate image
    img = cv2.warpAffine(img, rotate_mat, (w, w))

    # crop document
    return cv2.getRectSubPix(img, (w, h), center)
