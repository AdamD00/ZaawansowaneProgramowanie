import imutils
import numpy as np
import cv2

print("Write x, y")
x = int(input())
y = int(input())


image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
shifted = imutils.translate(image,x,y)
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)
