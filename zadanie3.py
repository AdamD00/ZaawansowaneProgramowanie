import cv2

# load the image and display it
image = cv2.imread("example.png")
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
block_size=[11,21,31,41]
names = ['MEAN','GAUSS']
for i in block_size:
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 10)

cv2.imshow("Mean Adaptive Thresholding Size 11", thresh_11)
cv2.imshow("Mean Adaptive Thresholding Size 21", thresh_21)
cv2.imshow("Mean Adaptive Thresholding Size 31", thresh_31)
cv2.imshow("Mean Adaptive Thresholding Size 41", thresh_41)
cv2.waitKey(0)