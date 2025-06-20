import cv2
import numpy as np

image = cv2.imread('image.png')
image = cv2.resize(image, (600, 400))
B, G, R = cv2.split(image)

cv2.imshow('Kanał Niebieski (Gray)', B)
cv2.imshow('Kanał Zielony (Gray)', G)
cv2.imshow('Kanał Czerwony (Gray)', R)

zeros = np.zeros_like(B)
blue_img = cv2.merge([B, zeros, zeros])
green_img = cv2.merge([zeros, G, zeros])
red_img = cv2.merge([zeros, zeros, R])

cv2.imshow('Kanał Niebieski (Kolor)', blue_img)
cv2.imshow('Kanał Zielony (Kolor)', green_img)
cv2.imshow('Kanał Czerwony (Kolor)', red_img)

cv2.imwrite('kanal_niebieski_gray.jpg', B)
cv2.imwrite('kanal_zielony_gray.jpg', G)
cv2.imwrite('kanal_czerwony_gray.jpg', R)

cv2.imwrite('kanal_niebieski_color.jpg', blue_img)
cv2.imwrite('kanal_zielony_color.jpg', green_img)
cv2.imwrite('kanal_czerwony_color.jpg', red_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
