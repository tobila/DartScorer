# -*- coding: utf-8 -*-
import cv2
import numpy as np
import math;
from range_key_dict import RangeKeyDict

# Ursprung; Positive X-Achse hat 0-Grad, steigerung im Uhrzeigersinn
# https://math.stackexchange.com/questions/707673/find-angle-in-degrees-from-one-point-to-another-in-2d-space
# x1 = 300;
# y1 = 300;
#
# # Punkt
# x2 = 300;
# y2 = 100;
#
# x = x2-x1;
# y = y2-y1;
#
# # Winkel als Radiant
# angle = math.atan2(y,x);
# print angle;
#
# # Winkel in Grad von 0-360
# theta = math.degrees(math.atan2(y, x));
# if (theta < 0.0):
#     theta += 360.0;
# print theta;


##############
segmentArea = RangeKeyDict({
    (-9,9): 6,
    (9,27): 10,
    (27,45): 15,
    (45,63): 2,
    (63,81): 17,
    (81,99): 3,
    (99,117): 19,
    (117,135): 7,
    (135,153): 16,
    (153,171): 8,
    (171,181): 11,
    (-180,-171): 11,
    (-171,-153): 14,
    (-153,-135): 9,
    (-135,-117): 12,
    (-117,-99): 5,
    (-99,-81): 20,
    (-81,-63): 1,
    (-63,-45): 18,
    (-45,-27): 4,
    (-27,-9): 13
})

# Dartboard Durchmesser=34cm; in Pixel (für 72dpi) = 964px
# 340mm - 964       -> Durchmesser Dartboard
# 1mm - 2,8352941176
# 31,8mm - 90,16    -> Durchmesser SingelBull
# 12,7mm - 36,01    -> Durchmesser Bull
# 8mm - 22,68       -> Breite Double+Tripple Felder
# 107mm - 303,38    -> Abstand äußerer Tripple-Ring
radiusBoard = 964/2
double = (radiusBoard, radiusBoard-22,68)
single1 = (double[0], 303,38)
tripple = (single1[1], single1[1]-22,68)
single2 = (tripple[1], 45)
singleBull = (single2[1], 18)
bull = (singleBull[1], 0)

def getSegmentOfCoordinates(dartPosition, boardCenter):
    x = dartPosition[0] - boardCenter[0]
    y = dartPosition[1] - boardCenter[1]

    # Winkel als Radiant
    angle = math.atan2(y,x)

    # Winkel in Grad von -180 bis 180
    theta = math.degrees(math.atan2(y, x));

    # Abstand von dartPosition zu boardCenter
    distance = math.sqrt(math.pow(x,2) + math.pow(y,2))
    points = 0

    if distance > radiusBoard:
        points = 0
    elif double[0] > distance >= double[1]:
        points = segmentArea[theta] * 2
    elif single1[0] > distance >= single1[1]:
        points = segmentArea[theta]
    elif tripple[0] > distance >= tripple[1]:
        points = segmentArea[theta] * 3
    elif single2[0] > distance >= single2[1]:
        points = segmentArea[theta]
    elif singleBull[0] > distance >= singleBull[1]:
        points = 25
    elif bull[0] > distance >= bull[1]:
        points = 50
    else:
        points = 0


    print (distance)
    print (segmentArea[theta])
    print (points)
