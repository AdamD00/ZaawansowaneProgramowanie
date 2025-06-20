import cv2
import numpy as np

image_path = "image.jpg"
image = cv2.imread(image_path)
scale_ratio = 300 / image.shape[1]
new_dim = (300, int(image.shape[0] * scale_ratio))
resized = cv2.resize(image, new_dim)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

min_area = 500
max_area = 5000

filtered_contours = [cnt for cnt in contours if min_area <= cv2.contourArea(cnt) <= max_area]

widths = []
heights = []

for i, cnt in enumerate(filtered_contours, 1):
    x, y, w, h = cv2.boundingRect(cnt)
    widths.append(w)
    heights.append(h)
    cx, cy = x + w // 2, y

    cv2.putText(resized, f"{i}", (cx - 10, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.rectangle(resized, (x, y), (x + w, y + h), (255, 0, 0), 2)
    dim_text = f"{w}x{h} px"
    cv2.putText(resized, dim_text, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

cv2.imshow("Filtrowane kostki", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

if filtered_contours:
    avg_width = np.mean(widths)
    avg_height = np.mean(heights)
    min_width = np.min(widths)
    max_width = np.max(widths)
    min_height = np.min(heights)
    max_height = np.max(heights)

    print(f"Liczba wykrytych kostek: {len(filtered_contours)}")
    print(f"Średnia szerokość: {avg_width:.2f} px")
    print(f"Średnia wysokość: {avg_height:.2f} px")
    print(f"Minimalna szerokość: {min_width} px")
    print(f"Maksymalna szerokość: {max_width} px")
    print(f"Minimalna wysokość: {min_height} px")
    print(f"Maksymalna wysokość: {max_height} px")
else:
    print("Nie wykryto kostek spełniających kryteria filtracji.")
