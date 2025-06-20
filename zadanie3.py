import cv2
import numpy as np

image_path = "image.png"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, binary = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)
eroded = cv2.erode(binary, kernel, iterations=1)

cv2.imshow("Binaryzny obraz przed erozją", binary)
cv2.imshow("Obraz po erozji", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Opis efektu:
# Po erozji białe obszary w obrazie binarnym ulegają pomniejszeniu — obiekty stają się
# cieńsze, a małe zakłócenia (szum) są redukowane lub całkowicie usuwane.
# Dzięki temu erozja pomaga w eliminacji drobnych artefaktów i wygładzaniu krawędzi.
