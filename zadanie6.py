import cv2
import numpy as np

image_path = "example.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((3,3), np.uint8)
eroded = cv2.erode(binary, kernel, iterations=1)
dilated = cv2.dilate(binary, kernel, iterations=1)
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Oryginalny", image)
cv2.imshow("Binaryzowany", binary)
cv2.imshow("Erozja", eroded)
cv2.imshow("Dylacja", dilated)
cv2.imshow("Otwarcie", opened)
cv2.imshow("Zamkniecie", closed)

cv2.waitKey(0)
cv2.destroyAllWindows()
