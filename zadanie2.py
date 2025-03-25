import cv2
import numpy as np


image = cv2.imread("example.jpg")
M = np.ones(image.shape, dtype="uint8") * 150
added = cv2.add(image, M)
cv2.imshow("Lighter", added)
M = np.ones(image.shape, dtype="uint8") * 150
addedNumpy = np.add(image,M)
cv2.imshow("Darker", addedNumpy)
cv2.waitKey(0)
