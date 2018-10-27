# import the necessary packages
import numpy as np
import argparse
import glob
import cv2


# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--images", required=True,
# 	help="path to input dataset of images")
# args = vars(ap.parse_args())

# loop over the images
# for imagePath in glob.glob(args["images"] + "/*.jpg"):

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread('IMG_6466.jpeg')

lower_red = np.array([150,0,0])  # BGR-code of your lowest red
upper_red = np.array([255,80,80])   # BGR-code of your highest red
mask = cv2.inRange(image, lower_red, upper_red)
#get all non zero values
coord=cv2.findNonZero(mask)
print mask
print coord
cv2.circle(image,(2843,980),1,(255,255,255),-1)
# show the images
cv2.imshow("Original", image)
# cv2.imshow("Edges", np.hstack([wide, tight, auto]))
cv2.waitKey(0)
