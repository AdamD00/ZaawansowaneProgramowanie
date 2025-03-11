import cv2

image = cv2.imread('image.jpg')
cv2.imshow("Orginal",image)
(h, w) = image.shape[:2]
image[h-1,w-1] = (0,0,255)
cv2.imshow("Updated", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
