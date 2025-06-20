import cv2
import numpy as np

image_path = "cat.jpg"
image = cv2.imread(image_path)


mask = np.zeros(image.shape[:2], dtype=np.uint8)
x, y, w, h = 100, 50, 200, 200
mask[y:y+h, x:x+w] = 255

blurred = cv2.GaussianBlur(image, (25, 25), 0)

foreground = cv2.bitwise_and(image, image, mask=mask)
background = cv2.bitwise_and(blurred, blurred, mask=cv2.bitwise_not(mask))
result = cv2.add(foreground, background)

cv2.imshow("Oryginalny", image)
cv2.imshow("Efekt głębi ostrości", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
