import cv2
import numpy as np


image = cv2.imread('image.jpg')
image = cv2.resize(image, (600, 400))


lower = np.array([20, 40, 100])
upper = np.array([70, 80, 160])

mask = cv2.inRange(image, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)


cv2.imshow('Oryginalny obraz', image)
cv2.imshow('Maska', mask)
cv2.imshow('Wynik z wybranym kolorem', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
