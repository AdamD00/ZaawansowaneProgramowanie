import cv2
import imutils

# load the original input image and display it on our screen
image = cv2.imread("example.jpg")
cv2.imshow("Original", image)

(w,h) = image.shape[:2]

resize = imutils.resize(image,width=w//2,height=h//2)
cv2.imshow("Half",resize)
cv2.waitKey(0)