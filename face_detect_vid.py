import cv2 as cv

# capture video from camera
capture = cv.VideoCapture(0)

# reading haar xml file
haar_cascade = cv.CascadeClassifier("haar_face.xml")

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # detect the face
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,
                                               minNeighbors=7)

    # drawing a rectangle over faces
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    cv.imshow("Detected Faces", frame)
    if (cv.waitKey(1) & 0xFF == ord("q")):
        break


capture.release()
cv.destroyAllWindows()
