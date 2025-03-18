import cv2

img = cv2.imread("image.jpg")
(h,w) = img.shape[:2]
top = img[:h,:w//2]

bottom = img[:h,w//2:w]
cv2.imshow("R",bottom)
cv2.waitKey(0)