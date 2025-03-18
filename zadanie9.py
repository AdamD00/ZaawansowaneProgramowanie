import argparse
import imutils
import cv2
image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

rotated = imutils.rotate(image, 75)
cv2.imshow("Rotated 75 Degrees", rotated)
cv2.waitKey(0)
cv2.imwrite("Rotated_image.jpg",rotated)