import cv2
import imutils
import math
# load the original input image and display it on our screen
image = cv2.imread("example.jpg")
cv2.imshow("Original", image)
for percent in range(100,300,20):
    i = math.ceil(percent/100)
    print(percent)

    resized = imutils.resize(image, width=image.shape[1]*i)
    cv2.imshow("Resized", resized)
    cv2.waitKey(500)

