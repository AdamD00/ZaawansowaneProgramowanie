import cv2
import numpy as np


image_path = 'image.png'
image = cv2.imread(image_path)

B, G, R = cv2.split(image)

R_boosted = cv2.add(R, 50)

image_boosted_R = cv2.merge([B, G, R_boosted])


cv2.imshow('Oryginalny obraz', image)
cv2.imshow('Obraz ze wzmocnionym kanałem R (+50)', image_boosted_R)

cv2.waitKey(0)
cv2.destroyAllWindows()
