# import the necessary packages
import cv2
# load the original input image and display it to our screen
image = cv2.imread("example.jpg")
cv2.imshow("Original", image)
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped  horizontally", flipped)
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Vertically and horizontally", flipped)
cv2.waitKey(0)