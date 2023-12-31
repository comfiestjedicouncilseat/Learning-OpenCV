import cv2 as cv

img = cv.imread("Photos/group 1.jpg")
cv.imshow("People", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray People", gray)

# reading haar xml file
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# detect the face
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,
                                           minNeighbors=1)

print(f"Number of faces found: {len(faces_rect)}")

# drawing a rectangle over faces
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow("Detected Faces", img)


cv.waitKey(0)
