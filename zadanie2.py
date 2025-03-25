import cv2
import numpy as np

triangle = np.zeros((300, 300), dtype="uint8")

pt1 = (0, 300)
pt2 = (150, 0)
pt3 = (300, 300)

triangle_cnt = np.array([pt1, pt2, pt3])

cv2.drawContours(triangle, [triangle_cnt], 0, (255,255,255), -1)

# finding centroid
centroid = ((pt1[0]+pt2[0]+pt3[0])//3, (pt1[1]+pt2[1]+pt3[1])//3)
cv2.circle(triangle, centroid, 2, (255, 255, 255))

cv2.imshow("Triangle", triangle)
triangle2 = np.zeros((300, 300), dtype="uint8")

pt1 = (0, 300)
pt2 = (200, 0)
pt3 = (300, 300)

triangle_cnt2 = np.array([pt1, pt2, pt3])

cv2.drawContours(triangle2, [triangle_cnt2], 0, (255,255,255), -1)

# finding centroid
centroid = ((pt1[0]+pt2[0]+pt3[0])//3, (pt1[1]+pt2[1]+pt3[1])//3)
cv2.circle(triangle2, centroid, 2, (255, 255, 255))

cv2.imshow("Triangle2", triangle2)
bitwiseXor = cv2.bitwise_xor(triangle,triangle2)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)