# import the necessary packages
import cv2
# load the original input image and display it to our screen
image = cv2.imread("example.jpg")
print("How to flip a cat? [-1,0,1]")
i = int(input())
flipped = cv2.flip(image, i)
cv2.imshow("Flipped Vertically", flipped)

cv2.waitKey(0)