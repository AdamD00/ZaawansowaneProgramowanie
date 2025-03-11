import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Orginal", image)
(h, w) = image.shape[:2]
image[50:100,50:100] = (255,255,255)
cv2.imshow("Updated", image)
cv2.waitKey(0)