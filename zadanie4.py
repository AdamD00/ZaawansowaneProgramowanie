import cv2

image_path = "cat.jpg"
image = cv2.imread(image_path)

blur_3 = cv2.blur(image, (3, 3))
blur_7 = cv2.blur(image, (7, 7))

gaussian_3 = cv2.GaussianBlur(image, (3, 3), 0)
gaussian_7 = cv2.GaussianBlur(image, (7, 7), 0)

median_3 = cv2.medianBlur(image, 3)
median_7 = cv2.medianBlur(image, 7)

bilateral_5 = cv2.bilateralFilter(image, 5, 75, 75)
bilateral_9 = cv2.bilateralFilter(image, 9, 150, 150)

cv2.imshow("Oryginalny", image)
cv2.imshow("Blur (3x3)", blur_3)
cv2.imshow("Blur (7x7)", blur_7)
cv2.imshow("Gaussian (3x3)", gaussian_3)
cv2.imshow("Gaussian (7x7)", gaussian_7)
cv2.imshow("Median (3)", median_3)
cv2.imshow("Median (7)", median_7)
cv2.imshow("Bilateral (5)", bilateral_5)
cv2.imshow("Bilateral (9)", bilateral_9)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Odpowiedzi:
# i. Które metody najmocniej rozmywają tekst?
#    -> Proste rozmycie (cv2.blur) i rozmycie Gaussa z dużym kernel'em (7x7) najmocniej rozmywają tekst.
# ii. Które pozwalają zachować jego czytelność?
#    -> Rozmycie medianowe i dwustronne (bilateralne) lepiej zachowują krawędzie, dzięki czemu tekst pozostaje bardziej czytelny.
