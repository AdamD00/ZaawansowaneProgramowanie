import cv2
import numpy as np

image_path = "image.png"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

bright = cv2.add(gray, 50)

_, thresh_original = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
_, thresh_bright = cv2.threshold(bright, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("Oryginalny", gray)
cv2.imshow("Rozjaśniony +50", bright)
cv2.imshow("Progowanie oryginalny", thresh_original)
cv2.imshow("Progowanie rozjaśniony", thresh_bright)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Komentarz:
# Zwiększenie jasności powoduje, że więcej pikseli przekracza wartość progową i
# jest interpretowanych jako pierwszy plan. Metoda progowania prosta jest czuła na
# zmiany oświetlenia, co może prowadzić do błędnego rozróżniania tła i obiektu.
# W praktyce stosuje się progowanie adaptacyjne lub metody uwzględniające oświetlenie.
