import cv2

image_path = "image.png"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
bright = cv2.add(gray, 50)

_, thresh_simple = cv2.threshold(bright, 100, 255, cv2.THRESH_BINARY)
_, thresh_otsu = cv2.threshold(bright, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Rozjaśniony obraz", bright)
cv2.imshow("Progowanie proste T=100", thresh_simple)
cv2.imshow("Progowanie metodą Otsu", thresh_otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Komentarz:
# Progowanie metodą Otsu automatycznie wybiera wartość progową, która najlepiej oddziela
# pierwszy plan od tła na podstawie histogramu. Dzięki temu jest mniej wrażliwe na zmiany
# oświetlenia niż progowanie proste z ustaloną wartością.
