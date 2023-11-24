import cv2 as cv


# rescales images and videos and live video
def rescaleFrame(frame, scale=0.75):
    # takes width value from frame and multiplies by scale
    width = int(frame.shape[1] * scale)
    # creates tuple with new width and height values
    height = int(frame.shape[0] * scale)
    # creates tuple with new width and height values
    dimensions = (width, height)

    # return resized frame; interpolation is method used for resizing,
    # cv.INTER_AREA is suitable for downsizing
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# rescales live video only
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


# select a video to read from
capture = cv.VideoCapture("Videos/dog.mp4")

# loop till break
while True:
    # read a single "pic" from the video, read frames
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    # display the frame in window
    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)
    # if "d" is pressed, break, each frame is displayed for 20 milliseconds
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# delete the capture variable
capture.release()
# close the display window
cv.destroyAllWindows()
