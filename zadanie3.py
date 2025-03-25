import cv2
import numpy as np


image = cv2.imread("example.jpg")
M = np.ones(image.shape, dtype="uint8") * 150
sub = cv2.subtract(image, M)
cv2.imshow("Lighter", sub)
M = np.ones(image.shape, dtype="uint8") * 150
subNumpy = np.subtract(image,M)
cv2.imshow("Darker", subNumpy)
cv2.waitKey(0)
