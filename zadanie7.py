import cv2

image_path = "image.png"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
bright = cv2.add(gray, 50)

_, mask = cv2.threshold(bright, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Maska binarna (Otsu)", mask)
cv2.imshow("Wycięty obiekt", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Komentarz:
# Obiekt jest często dobrze oddzielony, zwłaszcza gdy kontrast między nim a tłem jest
# wyraźny. Ograniczenia metody Otsu to słabsza skuteczność przy niestandardowym
# oświetleniu, słabym kontraście, lub gdy tło i obiekt mają podobne wartości intensywności.
# W takich przypadkach potrzebne są metody adaptacyjne lub segmentacja z wykorzystaniem cech.
