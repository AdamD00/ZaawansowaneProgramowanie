import cv2

img = cv2.imread("image.jpg")
(h,w) = img.shape[:2]
top = img[:h//2,:w]

bottom = img[h//2:h,:w]
cv2.imshow("LT",bottom)
cv2.waitKey(0)