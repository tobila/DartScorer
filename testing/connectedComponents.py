# https://stackoverflow.com/questions/46441893/connected-component-labeling-in-python
import cv2
import numpy as np

img = cv2.imread('testImg2.jpeg', 0)
# img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]  # ensure binary

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
dilation = cv2.dilate(erosion,kernel,iterations = 1)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


ret, labels = cv2.connectedComponents(dilation)

# Map component labels to hue val
label_hue = np.uint8(179*labels/np.max(labels))
blank_ch = 255*np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

# cvt to BGR for display
labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

# set bg label to black
labeled_img[label_hue==0] = 0

cv2.imshow('labeled.png', labeled_img)
cv2.waitKey()
