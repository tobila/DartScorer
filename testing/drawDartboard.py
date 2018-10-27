import cv2
import numpy as np
import math


def rotateImage(image, angle):
    center=tuple(np.array(image.shape[0:2])/2)
    rot_mat = cv2.getRotationMatrix2D(center,angle,1.0)
    return cv2.warpAffine(image, rot_mat, image.shape[0:2],flags=cv2.INTER_LINEAR)


# Create new black image
blank_img = np.zeros((600,600,3), np.uint8)

# Draw point
# cv2.circle(blank_img,(100,100),1,(255,255,255),-1)
# cv2.circle(blank_img,(100,200),1,(255,255,255),-1)
# cv2.circle(blank_img,(200,100),1,(255,255,255),-1)
# cv2.circle(blank_img,(200,200),1,(255,255,255),-1)

p1 = (100,100)
p2 = (500,500)
# center = (300,300)
center=tuple(np.array(blank_img.shape[0:2])/2)


# cv2.rectangle(blank_img,p1,p2,(0,255,0),1)
# cv2.circle(blank_img,(300,300),200,(255,0,0),1)
# cv2.line(blank_img,(100,100),(500,500),(0,0,255),1)
# cv2.line(blank_img,(100,500),(500,100),(0,0,255),1)

for angle in range(18,181,18):
    print angle
    rot_mat = cv2.getRotationMatrix2D(center,angle,1.0)
    rot_p1 = rot_mat.dot(np.array(p1 + (1,)))
    rot_p2 = rot_mat.dot(np.array(p2 + (1,)))
    cv2.line(blank_img,(int(rot_p1[0]),int(rot_p1[1])),(int(rot_p2[0]),int(rot_p2[1])),(0,0,255),1)


distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
radius = int(distance/2)
cv2.circle(blank_img,(300,300),radius,(255,255,255),1)
print "####"
print distance

# img = rotateImage(blank_img, 45)
# rotated_point = img.dot(np.array(p1 + (1,)))
# rotated_point2 = img.dot(np.array(p2 + (1,)))
# cv2.circle(blank_img,(int(rotated_point[0]),int(rotated_point[1])),1,(255,255,255), -1)
# cv2.circle(blank_img,(int(rotated_point2[0]),int(rotated_point2[1])),1,(255,255,255), -1)

cv2.imshow('blank', blank_img)
# cv2.imshow('rotate', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
