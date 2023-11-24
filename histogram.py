import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Grayscale Histogram
gray_hist = cv.calcHist(images=[gray],
                        channels=[0],
                        mask=None,
                        istSize=[256],
                        ranges=[0, 256])


cv.waitKey(0)
