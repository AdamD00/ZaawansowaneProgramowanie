import imutils
import numpy as np
import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
(h,w) = image.shape[:2]
M = np.float32([[1, 0, w//2], [0, 1, h//2]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)
