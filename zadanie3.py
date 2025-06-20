import cv2

image_path = "image.jpg"
image = cv2.imread(image_path)
gray_orig = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_value = 140

widths = [100, 200, 300, 500]

for w in widths:
    scale_ratio = w / image.shape[1]
    new_dim = (w, int(image.shape[0] * scale_ratio))
    resized = cv2.resize(image, new_dim)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_contours = resized.copy()
    cv2.drawContours(img_contours, contours, -1, (0, 0, 255), 2)

    print(f"Rozmiar obrazu: {w} px szerokości, liczba konturów: {len(contours)}")

    cv2.imshow(f"Kontury, szerokość={w}", img_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()
