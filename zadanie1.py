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
# draw a circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)
bitwiseAnd = cv2.bitwise_and(triangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)
bitwiseOr = cv2.bitwise_or(triangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)
bitwiseXor = cv2.bitwise_xor(triangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)
bitwiseNot = cv2.bitwise_not(triangle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)