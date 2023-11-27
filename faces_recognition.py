import cv2 as cv
import os

# This program takes face trained data and uses it for face recognition

# Creates a peoples list
people = []
DIR = r"C:\Users\Michael\Documents\Coding\OpenCVLearning\Faces\train"
for i in os.listdir(DIR):
    people.append(i)

# Activates the Haar Cascade classifier to detect faces on an image
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# Create the face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Have the face recognizer read the yaml file with the trained data
face_recognizer.read("face_trained.yml")

# Read the image that is to be recognized, change to grayscale
img = cv.imread(r"C:\Users\Michael\Documents\Coding"
                r"\OpenCVLearning\Faces\val\ben_afflek\2.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Find the face using Haar Cascades
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,
                                           minNeighbors=4)

# For every face found:
for (x, y, w, h) in faces_rect:
    # Define faces_roi as the cropped image of the face only
    faces_roi = gray[y:y + h, x:x + w]
    # Have the face recognized predict the face, give a label and confidence
    label, confidence = face_recognizer.predict(faces_roi)
    print(f"Label = {label} with a confidence of {confidence}")
    # Label the specific person's name on the image
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX,
               1.0, (0, 255, 0), thickness=2)
    # Draw a rectangle on their face
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

# Display the image with the face recognized
cv.imshow("Detected Face", img)

cv.waitKey(0)
