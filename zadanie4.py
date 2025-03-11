import argparse
import imutils
import cv2
from numpy import double
print("Write angle")
angle = double(input())
image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX,cY), angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by {} Degrees".format(angle), rotated)
cv2.waitKey(0)