# IMPORTS
import numpy as np
import cv2

#--------- Load Image ---------
ImgWithDart = cv2.imread('../img_vid/ScheibeMit.jpg' )
ImgWithoutDart = cv2.imread("../img_vid/ScheibeOhne.jpg")

#--------- Load Video ---------
cap = cv2.VideoCapture ("../img_vid/ThrowDart_Komp.MP4")

#--- createBackgroundSubtion
fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg.apply(ImgWithoutDart)
fgmask = fgbg.apply(ImgWithDart)

#--- Nois reduction
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(fgmask,kernel,iterations = 1)
# dilation = cv2.dilate(fgmask,kernel,iterations = 1)
opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

#--- Contures
ret,thresh = cv2.threshold(erosion,126,255,0)
im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

k = cv2.isContourConvex(cnt)
print (k)


#--- Processing Video
while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    #--- Nois reduction
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(fgmask,kernel,iterations = 1)
    # dilation = cv2.dilate(fgmask,kernel,iterations = 1)
    opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    #--- Contures
    # ret,thresh = cv2.threshold(erosion,126,255,0)
    # im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
    # cnt = contours[0]

    cv2.imshow('original', frame)
    cv2.imshow('erosion', erosion)
    cv2.imshow('kernel', kernel)
    cv2.imshow('opening', opening)
    cv2.imshow('fg', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break


#--- Output
cv2.namedWindow('erosion', cv2.WINDOW_NORMAL)
cv2.resizeWindow('erosion', 600,600)
cv2.imshow('erosion', erosion)

cv2.namedWindow('thresh', cv2.WINDOW_NORMAL)
cv2.resizeWindow('thresh', 600,600)
cv2.imshow('thresh', thresh)





#--------- Load Video ---------
# VideoCap = cv2.VideoCapture ("../img_vid/ThrowDart_Komp.MP4")




# End System
cv2.waitKey(0)
cv2.destroyAllWindows()
