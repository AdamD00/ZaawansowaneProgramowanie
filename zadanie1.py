import cv2

image_path = "image.jpg"
image = cv2.imread(image_path)

scale_ratio = 300 / image.shape[1]
new_dim = (300, int(image.shape[0] * scale_ratio))
resized = cv2.resize(image, new_dim)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

threshold_values = [100, 140, 180]

for T in threshold_values:
    _, thresh = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)
    cv2.imshow(f"Progowanie klasyczne T={T}", thresh)

cv2.imshow("Oryginalny obraz", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
