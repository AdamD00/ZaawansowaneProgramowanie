import cv2
import numpy as np

image_path = "cat.jpg"
image = cv2.imread(image_path)

noise = np.zeros_like(image, dtype=np.uint8)
cv2.randn(noise, (0,0,0), (30,30,30))  # średnia=0, sigma=30 dla każdego kanału
noisy_image = cv2.add(image, noise)

blur = cv2.blur(noisy_image, (5, 5))
gaussian = cv2.GaussianBlur(noisy_image, (5, 5), 0)
median = cv2.medianBlur(noisy_image, 5)
bilateral = cv2.bilateralFilter(noisy_image, 9, 75, 75)

cv2.imshow("Oryginalny", image)
cv2.imshow("Obraz z szumem gaussowskim", noisy_image)
cv2.imshow("Rozmycie proste", blur)
cv2.imshow("Rozmycie Gaussa", gaussian)
cv2.imshow("Rozmycie medianowe", median)
cv2.imshow("Rozmycie bilateralne", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
