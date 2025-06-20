import cv2

image_path = "image.png"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh_30 = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
_, thresh_100 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
_, thresh_200 = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

cv2.imshow("Oryginalny", image)
cv2.imshow("Progowanie T=30", thresh_30)
cv2.imshow("Progowanie T=100", thresh_100)
cv2.imshow("Progowanie T=200", thresh_200)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Która wartość najlepiej oddziela pierwszy plan od tła?
# Zależy od obrazu. Zwykle wartość progowa dobierana jest eksperymentalnie.
#    T=100 jest często dobrym punktem startowym, ale warto użyć metody adaptacyjnej lub Otsu dla automatycznego doboru.
# W tym przykładzie T = 30 wygląda dobrze
