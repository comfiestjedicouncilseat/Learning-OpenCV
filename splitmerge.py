import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

# blank image for making a single color image
blank = np.zeros(img.shape[:2], dtype="uint8")

# splitting image into three seperate images, each with one color channel
b, g, r = cv.split(img)

# using blank to create a colored single channel image
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# show single channel image, but as grayscale (white = more intense)
cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

# display the three colored single channel images
cv.imshow("Blue_Single", blue)
cv.imshow("Green_Single", green)
cv.imshow("Red_Single", red)

# print statements for the shape (pretty much just for showing that img has a
# third parameter; channel)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merging the three grayscale single channel images into a bgr image
merged = cv.merge([b, g, r])
cv.imshow("Merged", merged)


cv.waitKey(0)
