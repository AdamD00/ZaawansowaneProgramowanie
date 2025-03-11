import argparse
import imutils
import cv2
image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

rotated = imutils.rotate(image, 30)
rotated = imutils.rotate(rotated, 30)
rotated = imutils.rotate(rotated, 30)

cv2.imshow("Rotated 3*30 Degrees", rotated)
rotated = imutils.rotate(image, 90)
cv2.imshow("Rotated 90 Degrees", rotated)

cv2.waitKey(0)