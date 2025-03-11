import cv2
import numpy as np

canvas = np.zeros((400,400, 3), dtype="uint8")

# draw a green line from the top-left corner of our canvas to the
# bottom-right
blue = (255, 0, 0)
red = (0, 0, 255)
green = (0,255,0)
cv2.rectangle(canvas,(0,0),(100,50),green)
cv2.rectangle(canvas,(300,300),(400,400),red,4)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)