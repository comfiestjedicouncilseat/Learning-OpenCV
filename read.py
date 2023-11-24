import cv2 as cv

# displaying a picture (jpg)
# img = cv.imread("Photos/cat_large.jpg")       # read
# cv.imshow("WindowName", img)                  # display in window
# waitKey(0)                                    # do nothing, wait for a key to be pressed

# displaying a video
capture = cv.VideoCapture("Videos/dog.mp4")         # select a video to read from

while True:                                         # loop till break  
    isTrue, frame = capture.read()                  # read a single "pic" from the video, read frames
    cv.imshow("Video", frame)                       # display the frame in window
    if cv.waitKey(20) & 0xFF==ord('d'):             # if "d" is pressed, break, each frame is displayed for 20 milliseconds
        break

capture.release()                                   # delete the capture variable
cv.destroyAllWindows()                              # close the display window