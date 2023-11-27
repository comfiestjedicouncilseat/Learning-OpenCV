import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("Blank", blank)

# 1. paint the image a certain color
# blank[100:300] = 0, 255, 0
# cv.imshow("Green", blank)

# 2. draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=-1)
cv.imshow("Rectangle", blank)

# 3. draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 200,
          (0, 0, 255), thickness=2)
cv.imshow("Circle", blank)

# 4. draw a line
cv.line(blank, (125, 125), (375, 200), (255, 255, 255), thickness=5)
cv.imshow("Line", blank)

# 5. write text
cv.putText(blank, "Yo, what's poppin", (0, 255), cv.FONT_HERSHEY_TRIPLEX,
           1.0, (255, 255, 0), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)