import cv2
import numpy as np

canvas = np.zeros((300,300, 3), dtype="uint8")

(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

# loop over increasing radii, from 0 pixels to 150 pixels in 25
# pixel increments
for r in range(0, 180, 20):
# draw a white circle with the current radius size
    cv2.rectangle(canvas,(centerX-r,centerY-r),(centerX+r,centerY+r), white)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)