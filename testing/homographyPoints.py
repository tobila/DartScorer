import cv2
import numpy as np


# Read source image.
im_src = cv2.imread('videoV3/cam1_1.jpg')
# Four corners of the book in source image
pts_src = np.array([[79, 227],[114,145],[190,93],[294,58],[411,50], [535, 61],[658,91],[778,137],[890,196],[991,264],[1074, 343],[1127,429],[1144,518],[1111,600],[1011,662],[842, 685],[618,654],[387,570],[207,453],[104,333]])


# Read destination image.
im_dst = cv2.imread('img/drawDartboard.jpg')
# Four corners of the book in destination image.
pts_dst = np.array([[24, 425],[71,281],[159,159],[281,71],[425,24],[575, 24],[719,71],[841,159],[929,281],[976,425],[976, 575],[929,719],[841,841],[719,929],[575,976],[425, 976],[281,929],[159,841],[71,719],[24,575]])

# Calculate Homography
h, status = cv2.findHomography(pts_src, pts_dst)

# Warp source image to destination based on homography
im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))

# Display images
cv2.imshow("Source Image", im_src)
cv2.imshow("Destination Image", im_dst)
cv2.imshow("Warped Source Image", im_out)
# cv2.imwrite("warpedMitPfeil_2.jpg", im_out)

cv2.waitKey(0)
