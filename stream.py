
import cv2          # you require OpenCV 3.2 to be installed.

import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('example.mp4')  # change the example.mp4 with your own video file

try:
    if not os.path.exists('media'):
        os.makedirs('media')
except OSError:
    print ('Error: Creating directory of media')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './media/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To have unique image
    currentFrame += 1

# When everything done, release the cap
cap.release()
cv2.destroyAllWindows()