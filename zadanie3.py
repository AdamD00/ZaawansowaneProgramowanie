import cv2

image_path = "cat.jpg"
image = cv2.imread(image_path)

bilateral_1 = cv2.bilateralFilter(image, 5, 25, 25)
bilateral_2 = cv2.bilateralFilter(image, 9, 75, 75)
bilateral_3 = cv2.bilateralFilter(image, 15, 150, 150)

blur = cv2.blur(image, (9, 9))
gaussian = cv2.GaussianBlur(image, (9, 9), 0)
median = cv2.medianBlur(image, 9)

cv2.imshow("Oryginalny", image)
cv2.imshow("Rozmycie proste", blur)
cv2.imshow("Rozmycie Gaussa", gaussian)
cv2.imshow("Rozmycie medianowe", median)
cv2.imshow("Bilateral (5,25,25)", bilateral_1)
cv2.imshow("Bilateral (9,75,75)", bilateral_2)
cv2.imshow("Bilateral (15,150,150)", bilateral_3)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Odpowiedzi:
# i. Czy rozmycie dwustronne skutecznie redukuje szum?
#    -> Tak, szczególnie dla większych wartości sigmaColor i sigmaSpace.
# ii. Czy zachowuje lepiej krawędzie w porównaniu do innych metod?
#    -> Tak, rozmycie dwustronne zachowuje krawędzie znacznie lepiej niż blur, gaussian i median.
# iii. Jakie wartości parametrów dają najlepsze rezultaty?
#    -> Dla zdjęć z wyraźnym szumem i ostrymi krawędziami: (9,75,75) zapewnia dobrą równowagę między redukcją szumu a zachowaniem detali.
