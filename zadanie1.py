import cv2

#Wczytanie obrazu
image = cv2.imread("image.jpg")
image2 = cv2.imread("image1.jpg")
if image is None:
    print("Błąd: nie można odczytać")
else:
    print("Obraz wczytano")
if image2 is None:
    print("Błąd: nie można odczytać")
else:
    print("Obraz wczytano")