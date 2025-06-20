import cv2
import numpy as np


image_path = 'image.png'
image = cv2.imread(image_path)


B, G, R = cv2.split(image)


cv2.imshow('Oryginalny obraz (BGR)', image)
cv2.imshow('Kanał Czerwony (R)', R)
cv2.imshow('Kanał Zielony (G)', G)
cv2.imshow('Kanał Niebieski (B)', B)


mask_r = (R > 150) & (G < 100) & (B < 100)
mask_g = (G > 150) & (R < 100) & (B < 100)
mask_b = (B > 150) & (R < 100) & (G < 100)


mask_r_img = np.uint8(mask_r) * 255
mask_g_img = np.uint8(mask_g) * 255
mask_b_img = np.uint8(mask_b) * 255

cv2.imshow('Widoczne tylko w kanale R', mask_r_img)
cv2.imshow('Widoczne tylko w kanale G', mask_g_img)
cv2.imshow('Widoczne tylko w kanale B', mask_b_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
