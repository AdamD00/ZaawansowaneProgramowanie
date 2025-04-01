import cv2

image = cv2.imread('exampleThin.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
kernelElipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
kernelRect = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
dilatedElipse = cv2.dilate(gray.copy(),kernelElipse)
dilatedRect = cv2.dilate(gray.copy(),kernelRect)
cv2.imshow("Dilated Rect",dilatedRect)
cv2.imshow("Dilated Elipse",dilatedElipse)
cv2.waitKey(0)
