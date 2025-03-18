import cv2
import imutils

# load the original input image and display it on our screen
image = cv2.imread("example.jpg")
cv2.imshow("Original", image)

(w,h) = image.shape[:2]

resized = cv2.resize(image, (200,300), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized", resized)
cv2.waitKey(0)