import cv2
#Wczytanie obrazu
image = cv2.imread("image.jpg")

if image is None:
    print("Błąd: nie można odczytać")
else:
    print("Obraz wczytano")

w,h,c = image.shape

print(f'Channels: {c}')