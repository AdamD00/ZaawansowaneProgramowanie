import cv2
import os

image_path = "image.jpg"
image = cv2.imread(image_path)
scale_ratio = 300 / image.shape[1]
new_dim = (300, int(image.shape[0] * scale_ratio))
resized = cv2.resize(image, new_dim)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output_dir = "kostki_wyciecia"
os.makedirs(output_dir, exist_ok=True)

for i, cnt in enumerate(contours, 1):
    x, y, w, h = cv2.boundingRect(cnt)
    cx, cy = x + w // 2, y  # środek nad kostką

    cv2.putText(resized, f"{i}", (cx - 10, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # wycinanie kostki z oryginalnego (skalowanego) obrazu
    kostka = resized[y:y+h, x:x+w]
    filename = os.path.join(output_dir, f"kostka_{i:02d}.png")
    cv2.imwrite(filename, kostka)

cv2.imshow("Numerowane kostki", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
