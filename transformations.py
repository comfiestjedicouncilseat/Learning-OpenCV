import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")

cv.imshow("Park", img)


# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, -100, 100)
cv.imshow("Translated", translated)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]    # Takes first two values of img.shape
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale=1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 70)
cv.imshow("Rotated", rotated)


# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)


# Flipping
flipped = cv.flip(img, -1)   # 0: vertical, 1: horizontal, -1: both
cv.imshow("Flipped", flipped)


# Cropping
cropped = img[200:400, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
