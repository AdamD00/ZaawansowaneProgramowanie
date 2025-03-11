import argparse
import imutils
import cv2
image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
# rotate our image by 45 degrees around the center of the image
M = cv2.getRotationMatrix2D((cX,cY), 60, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 60 Degrees", rotated)
rotated = imutils.rotate(image, 60)
cv2.imshow("Rotated 60 Degrees", rotated)
cv2.waitKey(0)