import cv2
import imutils

# load the original input image and display it on our screen
image = cv2.imread("example.jpg")
cv2.imshow("Original", image)

resized = imutils.resize(image, height=400)
cv2.imshow("Resized", resized)
cv2.waitKey(0)