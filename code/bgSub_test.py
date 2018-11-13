import cv2
import numpy as np

# original video - too big
#cap = cv2.VideoCapture ("../img_vid/ThrowDart.MP4")

# smaller file
cap = cv2.VideoCapture ("../img_vid/ThrowDart_Komp.MP4")

fgbg = cv2.createBackgroundSubtractorMOG2()


while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('fg', fgmask)

    # cv2.namedWindow('oriiginal', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('oriiginal', 600,600)
    # cv2.imshow('oriiginal', frame)

    # cv2.namedWindow('fg', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('fg', 600,600)
    # cv2.imshow('fg', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
