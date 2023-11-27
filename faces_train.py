import os
import cv2 as cv
import numpy as np

# This program trains faces based on pictures contained within specific folders

# Created a list for the people, and the directory path to the folders with
# the pictures
people = []
DIR = r"C:\Users\Michael\Documents\Coding\OpenCVLearning\Faces\train"
# For all the folders in the "Faces\train" directory, append the name to the
# people list
for i in os.listdir(DIR):
    people.append(i)

# Activate the Haar Cascade classifier
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# Empty list to hold the "features" and "labels" of the pictures
features = []
labels = []


# Function for setting up the face training
def create_train():
    # For every person in the people list
    for person in people:
        # Obtain the path to the person's folder, and give them a label
        path = os.path.join(DIR, person)
        label = people.index(person)

        # For every image in the person's folder
        for img in os.listdir(path):
            # Obtain the path to the image
            img_path = os.path.join(path, img)

            # Have CV read the image using the path, turn to grayscale
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # Find the face using the Haar Cascade
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,
                                                       minNeighbors=4)

            # For every "face" detected by the Haar Cascade
            for (x, y, w, h) in faces_rect:
                # faces_roi is the cropped version of the image
                faces_roi = gray[y:y + h, x:x + w]
                # Append the faces_roi image to features
                features.append(faces_roi)
                # Append the corresponding label to the labels list
                labels.append(label)


# Run the function, train on the images
create_train()

# Convert the features and labels lists to np arrays
features = np.array(features, dtype="object")
labels = np.array(labels)

# Create the face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the face recognizer on the array of features and labels
face_recognizer.train(features, labels)

# Save the trained data to a yaml file
face_recognizer.save("face_trained.yml")
# Save the features and labels arrays to npy files
# np.save("features.npy", features)
# np.save("labels.npy", labels)
