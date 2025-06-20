import cv2

image_path = "example.png"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

mask = cv2.adaptiveThreshold(gray, 255,
                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY_INV,
                             11, 5)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Maska ROI (pierwszy plan)", mask)
cv2.imshow("Wyodrębnione obiekty", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
