import cv2
#Wczytanie obrazu
image = cv2.imread("image.jpg",cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Błąd: nie można odczytać")
else:
    print("Obraz wczytano")

cv2.imwrite('gray.jpg', image)