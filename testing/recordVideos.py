import numpy as np
import cv2

cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)
frame_width = int(cap1.get(3))
frame_height = int(cap2.get(4))
out1 = cv2.VideoWriter('2out1_130119.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 5, (frame_width,frame_height))
out2 = cv2.VideoWriter('2out2_130119.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 5, (frame_width,frame_height))

while(True):
    # Capture frame-by-frame
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    out1.write(frame1)
    out2.write(frame2)
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame1',frame1)
    cv2.imshow('frame2',frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap1.release()
out1.release()
cap2.release()
out2.release()
cv2.destroyAllWindows()
