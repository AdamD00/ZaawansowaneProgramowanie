import cv2

image_path = "image.png"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

_, thresh_no_blur = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
_, thresh_blur = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("Oryginalny szary", gray)
cv2.imshow("Rozmyty szary", blurred)
cv2.imshow("Progowanie bez rozmycia", thresh_no_blur)
cv2.imshow("Progowanie po rozmyciu", thresh_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Komentarz:
# Rozmycie Gaussa pomaga wygładzić szum i nierówności w obrazie, co często poprawia
# jakość progowania — krawędzie stają się mniej poszarpane, a wynik binarny bardziej spójny.
# Jednak zbyt duże rozmycie może zbytnio rozmyć szczegóły pierwszego planu.
