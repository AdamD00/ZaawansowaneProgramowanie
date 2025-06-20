import cv2
import numpy as np

image_path = 'image.png'
image = cv2.imread(image_path)

B, G, R = cv2.split(image)


reconstructed_rbg = cv2.merge([R, B, G])
cv2.imshow('Obraz z kanałami w kolejności R, B, G', reconstructed_rbg)

zeros = np.zeros_like(B)
image_no_red = cv2.merge([B, G, zeros])
image_no_green = cv2.merge([B, zeros, R])
image_no_blue = cv2.merge([zeros, G, R])

cv2.imshow('Obraz bez czerwonego kanału', image_no_red)
cv2.imshow('Obraz bez zielonego kanału', image_no_green)
cv2.imshow('Obraz bez niebieskiego kanału', image_no_blue)

cv2.waitKey(0)
cv2.destroyAllWindows()