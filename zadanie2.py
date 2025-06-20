import cv2

image_path = "cat.jpg"
image = cv2.imread(image_path)

kernel_sizes = [(3, 3), (5, 5), (9, 9), (15, 15)]

for k in kernel_sizes:
    blur = cv2.blur(image, k)
    gaussian = cv2.GaussianBlur(image, k, 0)
    ksize = k[0]
    median = cv2.medianBlur(image, ksize)
    bilateral = cv2.bilateralFilter(image, ksize * 2, 75, 75)

    cv2.imshow(f"Rozmycie proste {k}", blur)
    cv2.imshow(f"Rozmycie Gaussa {k}", gaussian)
    cv2.imshow(f"Rozmycie medianowe {k}", median)
    cv2.imshow(f"Rozmycie bilateralne {k}", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Odpowiedzi:
# i. Jak zmienia się efekt rozmycia w zależności od wielkości kernela?
#    -> Im większy kernel, tym silniejsze rozmycie. Zwiększa się rozmycie tła i krawędzie stają się mniej ostre.
# ii. Jaki rozmiar kernela jest optymalny dla redukcji szumu bez utraty istotnych detali?
#    -> Zwykle 5x5 lub 9x9 zapewnia dobrą równowagę – medianBlur dobrze usuwa szum impulsowy, a bilateralFilter zachowuje krawędzie.