import cv2
import numpy as np
image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
mask = np.zeros(image.shape[:2], dtype="uint8")
print(image.shape[:2])
cv2.rectangle(mask, (30,5), (150,150), 255, -1)
cv2.imshow("Rectangular Mask", mask)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)