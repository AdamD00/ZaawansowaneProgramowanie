#Zamykanie niezależne okienek

import cv2

#Wczytanie obrazu
image = cv2.imread("image.jpg")
#Wczytanie odcieni szarości
image_grey = cv2.imread("image.jpg",cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Błąd: nie można odczytać")
else:
    print("Obraz wczytano")

(h,w,c) = image.shape[:3]

print(f'width: {w} pixel')
print(f'height: {h} pixels')
print(f'channels: {c}')

cv2.imshow("Kotek",image) # tworzenie okna
cv2.imshow("Kotek - w odcieniach",image_grey) # tworzenie okna
cv2.waitKey(0) # czeka na przycisk - okno się nie zamyka
cv2.destroyWindow("Kotek") # Zamyka okna
cv2.waitKey(0) # czeka na przycisk - okno się nie zamyka
cv2.destroyWindow("Kotek - w odcieniach") # Zamyka okna