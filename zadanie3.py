import cv2
#Wczytanie obrazu
image = cv2.imread("image.jpg",cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Błąd: nie można odczytać")
else:
    print("Obraz wczytano")

w,h = image.shape

print(f'Channels: {h}')