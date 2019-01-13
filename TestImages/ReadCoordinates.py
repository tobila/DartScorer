import numpy as np
import cv2

# Load an color image in grayscale
# img = cv2.imread('Calib/Left_This.jpg',0)

img = cv2.imread('Calib/Right_This.jpg')

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
