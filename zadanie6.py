import cv2
import numpy as np

image_path = "image.png"
image = cv2.imread(image_path)

B, G, R = cv2.split(image)

swapped = cv2.merge([R, G, B])
removed_blue = cv2.merge([np.zeros_like(B), G, R])

cv2.imshow("Oryginalne logo", image)
cv2.imshow("Zamienione kolory (R <-> B)", swapped)
cv2.imshow("Usunięty kanał niebieski", removed_blue)

cv2.waitKey(0)
cv2.destroyAllWindows()
