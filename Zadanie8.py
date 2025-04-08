import cv2
import numpy as np

image = cv2.imread('example.png')
image = cv2.resize(image, (600, 400))
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_blue = np.array([85, 30, 30])
upper_blue = np.array([145, 255, 255])
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])
mask_green = cv2.inRange(hsv, lower_green, upper_green)
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])

mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)

mask_red = cv2.bitwise_or(mask_red1, mask_red2)

combined_mask = cv2.bitwise_or(mask_blue, mask_green)
combined_mask = cv2.bitwise_or(combined_mask, mask_red)

result = cv2.bitwise_and(image, image, mask=combined_mask)

cv2.imshow('Oryginalny obraz', image)
cv2.imshow('Maska kolorów (RGB)', combined_mask)
cv2.imshow('Wykryte kolory', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
