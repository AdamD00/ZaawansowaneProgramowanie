import cv2
import numpy as np

image = cv2.imread("image.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


lower_bound = np.array([0, 120, 70])
upper_bound = np.array([10, 255, 255])


mask = cv2.inRange(hsv, lower_bound, upper_bound)


result = cv2.bitwise_and(image, image, mask=mask)


cv2.imshow("Original Image", image)
cv2.imshow("Mask", mask)
cv2.imshow("Extracted Color", result)

cv2.waitKey(0)
