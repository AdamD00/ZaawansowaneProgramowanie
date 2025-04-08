import cv2
import numpy as np

image = cv2.imread('download.jpg')
image = cv2.resize(image, (600, 400))
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_skin = np.array([0, 15, 60])
upper_skin = np.array([20, 165, 255])
mask = cv2.inRange(hsv, lower_skin, upper_skin)
result = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Oryginalny obraz', image)
cv2.imshow('Maska', mask)
cv2.imshow('Wynik z wybranym kolorem', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
