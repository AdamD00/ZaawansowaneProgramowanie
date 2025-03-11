import argparse
import imutils
import cv2
# load the image and show it
image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
# grab the dimensions of the image and calculate the center of the
# image
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
# rotate our image by 45 degrees around the center of the image
M = cv2.getRotationMatrix2D((0,0), 30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 30 Degrees", rotated)
cv2.waitKey(0)