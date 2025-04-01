import cv2

image = cv2.imread('example.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
kernelElipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(20,5))
kernelRect = cv2.getStructuringElement(cv2.MORPH_RECT,(20,5))
erodedElipse = cv2.erode(gray.copy(),kernelElipse)
erodedRect = cv2.erode(gray.copy(),kernelRect)
cv2.imshow("Eroded Rect",erodedRect)
cv2.imshow("Eroded Elipse",erodedElipse)
cv2.waitKey(0)
#Obiekty w erozji kwadratowej mają krawędzie proste a w eliptycznej mają krawędzie obłe