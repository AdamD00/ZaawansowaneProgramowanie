import cv2
import numpy as np

canvas = np.zeros((300,300, 3), dtype="uint8")

# draw a green line from the top-left corner of our canvas to the
# bottom-right
blue = (255, 0, 0)
red = (0, 0, 255)
green = (0,255,0)
cv2.circle(canvas,(40,40),40,blue)
cv2.circle(canvas,(150,150),60,red)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)