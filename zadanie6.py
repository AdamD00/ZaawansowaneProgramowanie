import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "image.png"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
bright = cv2.add(gray, 50)

_, thresh_otsu = cv2.threshold(bright, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
otsu_threshold = _  # wartość progowa wyliczona przez Otsu

hist = cv2.calcHist([bright], [0], None, [256], [0,256])

plt.figure(figsize=(8,5))
plt.title("Histogram skali szarości z wartością progową Otsu")
plt.xlabel("Intensywność pikseli")
plt.ylabel("Liczba pikseli")
plt.plot(hist, color='gray')
plt.axvline(x=otsu_threshold, color='r', linestyle='--', label=f"Próg Otsu = {otsu_threshold:.0f}")
plt.legend()
plt.show()

# Odpowiedź:
# Na histogramie często widać dwa wyraźne skupiska intensywności odpowiadające tłu i
# obiektowi. Metoda Otsu znajduje próg, który minimalizuje wariancję wewnątrzklasową,
# czyli najlepiej rozdziela te dwa zbiory.
