import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")

# draw a green line from the top-left corner of our canvas to the
# bottom-right
blue = (255, 0, 0)
cv2.line(canvas, (150, 150), (300, 300), blue,2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)