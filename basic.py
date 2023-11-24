import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

# 1. convert image to grayscale
# For extracting the color intensity of an image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# 2. blur an image
# Gets rid of noise
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# 3. edge cascade
# Finds the edges in an image
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

# 4. dilate an image (with structuring element)
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Dilated", dilated)

# 5. eroding
# reverse of dilating
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow("Eroded", eroded)

# 6. resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# 7. cropping
# gonna use array slicing
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
