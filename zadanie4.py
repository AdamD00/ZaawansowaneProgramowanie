import cv2
import numpy as np

image = cv2.imread('gap.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Orginal",image)
kernel = np.ones((3,3),np.uint8)
dilated_img = cv2.dilate(gray, kernel, iterations = 2)

cv2.imshow("filled gaps for contour detection", dilated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()