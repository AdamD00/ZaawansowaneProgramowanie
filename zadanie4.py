import cv2
import numpy as np


image = cv2.imread("example.jpg")
R = np.ones(image.shape, dtype="uint8")* 20
added = cv2.add(image[:,:,0], R)
cv2.imshow("Lighter", added)

cv2.waitKey(0)
