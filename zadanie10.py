import argparse
import imutils
import cv2
image = cv2.imread("image.jpg")
#cv2.imshow("Original", image)
for i in range(0,360,15):
    rotated = imutils.rotate(image, i)
    cv2.imshow("Rotated 90 Degrees", rotated)
    cv2.waitKey(500)
