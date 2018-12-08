import cv2
import numpy as np
import homographyCam1

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('./video v3/out2.avi')

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

# Read until video is completed
counter = 0
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    counter+=1
    # Display the resulting frame
    warpedFrame = homographyCam1.warpCam1(frame)
    cv2.imshow('Frame',warpedFrame)
    # cv2.imwrite('videoV3/img_%d.jpg'%counter,frame)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else:
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
