import numpy as np
import cv2

fgbg = cv2.createBackgroundSubtractorMOG2(20, 30)

vid1 = cv2.VideoCapture('2out1_130119.avi' )
vid2 = cv2.VideoCapture('2out2_130119.avi' )
count = 0

while True:
    ret, frame1 = vid1.read()
    ret2, frame2 = vid2.read()

    fgmask = fgbg.apply(frame1)

    values = np.sum(fgmask == 255)
    # print ("Values: ", values)

    # One Dart
    # if values > 1000 and values < 10000:
    #     cv2.imwrite("left/frame%d.jpg" % count, frame1)
    #     cv2.imwrite("right/frame%d.jpg" % count, frame2)
    #     count += 1

    # Calib
    if values < 1000 and count < 10:
        cv2.imwrite("Calib/left%d.jpg" % count, frame1)
        cv2.imwrite("Calib/right%d.jpg" % count, frame2)
        count += 1

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

vid1.release()
cv2.destroyAllWindows()
