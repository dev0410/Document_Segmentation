import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_img(img):
    """
    ### description
    display img

    ### parameters
    img: image for displaying
    """
    plt.axis('off')
    plt.imshow(img)
    plt.show()


def get_contour(img):
    """
    ### description
    find and return contour of document in image.

    ### parameters
    img: original image with document

    ### return
    contour: contour of detected document
    """
	# convert BGR image to Gray Image
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

	# increase contrast
    gray = cv2.multiply(gray, np.array([1.25]))

	# apply blur
    gray = cv2.medianBlur(gray, 31, 0)

	# get adaptive threshold
    tresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 27, 7
    )

	# get edge
    edge = cv2.dilate(cv2.Canny(tresh, 0, 0), None)

	# find contour of document
    contour = sorted(
        cv2.findContours(edge,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[0], key=cv2.contourArea
    )[-1]

    return contour


def remove_background(img, contour):
    """
    ### description
    remove background of image and remain object

    ### parameters
    img: original image with document and background
    contour: region of object for remain

    ### return values
    res: image without background
    """
    # make a mask with the rectangle
    mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    cv2.drawContours(mask, [contour], -1, 255, cv2.FILLED)

	# apply mask to original image
    return cv2.bitwise_and(img, img, mask=mask)
