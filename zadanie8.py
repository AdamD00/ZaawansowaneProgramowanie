import cv2
import numpy as np

image_path = "image.png"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh_basic = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
_, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

blurred = cv2.GaussianBlur(gray, (5,5), 0)
_, thresh_otsu_blur = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernel = np.ones((3,3), np.uint8)
eroded = cv2.erode(thresh_otsu_blur, kernel, iterations=1)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Progowanie podstawowe T=120", thresh_basic)
cv2.imshow("Progowanie Otsu", thresh_otsu)
cv2.imshow("Progowanie Otsu po rozmyciu", thresh_otsu_blur)
cv2.imshow("Erozja po progowaniu Otsu + rozmyciu", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Komentarz:
# Progowanie metodą Otsu lepiej wykrywa wady, ponieważ automatycznie dobiera próg.
# Rozmycie Gaussa pomaga usunąć szum i wygładzić powierzchnię, a erozja usuwa drobne zakłócenia,
# dzięki czemu wady kostki są wyraźniejsze i bardziej czytelne na obrazie binarnym.
