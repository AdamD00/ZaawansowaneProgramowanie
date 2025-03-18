import cv2

img = cv2.imread("image.jpg")
rio = img[:100,:100]
cv2.imshow("LT",rio)
cv2.waitKey(0)