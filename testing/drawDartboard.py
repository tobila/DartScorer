# -*- coding: utf-8 -*-
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
import boardCalculations

# Create new white image
blank_img = np.ones((1000,1000,3), np.uint8)*255

# Draw Lines to an warped image instead of blank img:
# blank_img = cv2.imread('warpedMitPfeil_2.jpg')
# blank_img = cv2.cvtColor(blank_img, cv2.COLOR_BGR2RGB)

centerTmp=tuple(np.array(blank_img.shape[0:2])/2)
center = (int(centerTmp[0]),int(centerTmp[1]))

# distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
# radius = int(distance/2)

# Dartboard Durchmesser=34cm; in Pixel (für 72dpi) = 964px
# 340mm - 964       -> Durchmesser Dartboard
# 1mm - 2,8352941176
# 31,8mm - 90,16    -> Durchmesser SingelBull
# 12,7mm - 36,01    -> Durchmesser Bull
# 8mm - 22,68       -> Breite Double+Tripple Felder
# 107mm - 303,38    -> Abstand äußerer Tripple-Ring
radiusBoard = int(964/2);
cv2.circle(blank_img,center,radiusBoard,(0,255,255),1)
cv2.circle(blank_img,center,radiusBoard-22,(0,255,255),1)

radiusBull = int(36/2);
cv2.circle(blank_img,center,radiusBull,(0,255,255),1)

radiusSingleBull = int(90/2);
cv2.circle(blank_img,center,radiusSingleBull,(0,255,255),1)

radiusTriple = 303;
cv2.circle(blank_img,center,radiusTriple,(0,255,255),1)
cv2.circle(blank_img,center,radiusTriple-22,(0,255,255),1)


# x = center + r * cos(a)
# y = center + r * sin(a)
def getLineCoordinates(degrees):
    x1 = int(round(center[0] + radiusBoard * math.cos(math.radians(degrees))))
    y1 = int(round(center[0] + radiusBoard * math.sin(math.radians(degrees))))
    x2 = int(round(center[0] + radiusSingleBull * math.cos(math.radians(degrees))))
    y2 = int(round(center[0] + radiusSingleBull * math.sin(math.radians(degrees))))
    return (x1,y1),(x2,y2)



for angle in range(-171,180,18):
    coordinates = getLineCoordinates(angle)
    # print angle
    cv2.line(blank_img,coordinates[0],coordinates[1],(0,255,255),1)
    print(coordinates[0])

# print pyautogui.position()


########### boardCalculations test
boardCalculations.getSegmentOfCoordinates((500,500),center)
###########




plt.imshow(blank_img, 'gray'),plt.show()
# cv2.imwrite('outputImg/warpMitPfeil.jpg',blank_img)
# cv2.imshow('blank', blank_img)
# cv2.imshow('rotate', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
