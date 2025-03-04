#Rozmiary okien
import cv2

#Wczytanie obrazu
image = cv2.imread("image.jpg")


if image is None:
    print("Błąd: nie można odczytać")
else:
    print("Obraz wczytano")

cv2.namedWindow("Kotek", cv2.WINDOW_NORMAL)

cv2.imshow("Kotek",image) # tworzenie okna
cv2.waitKey(0) # czeka na przycisk - okno się nie zamyka
cv2.destroyAllWindow() # Zamyka okna


