import cv2

image_path = "cat.jpg"
image = cv2.imread(image_path)

blur = cv2.blur(image, (5, 5))
gaussian = cv2.GaussianBlur(image, (5, 5), 0)
median = cv2.medianBlur(image, 5)
bilateral = cv2.bilateralFilter(image, 9, 75, 75)

cv2.imshow("Oryginalny", image)
cv2.imshow("Rozmycie proste", blur)
cv2.imshow("Rozmycie Gaussa", gaussian)
cv2.imshow("Rozmycie medianowe", median)
cv2.imshow("Rozmycie bilateralne", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Odpowiedzi:
# i. Która metoda najlepiej usuwa szum?
#    -> Rozmycie medianowe najlepiej usuwa szum sol-pieprz.
# ii. Która metoda zachowuje najwięcej szczegółów?
#    -> Rozmycie bilateralne najlepiej zachowuje krawędzie i detale.
# iii. Zalety i wady:
#     - cv2.blur: szybkie, ale rozmazuje krawędzie.
#     - cv2.GaussianBlur: dobre ogólne wygładzenie, mniej artefaktów niż blur.
#     - cv2.medianBlur: bardzo dobre przy szumie impulsowym, może tracić detale.
#     - cv2.bilateralFilter: najlepsze zachowanie szczegółów, ale wolne obliczeniowo.