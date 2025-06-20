import cv2

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

for i, cnt in enumerate(filtered_contours, 1):
    x, y, w, h = cv2.boundingRect(cnt)
    cx, cy = x + w // 2, y

    cv2.putText(resized, f"{i}", (cx - 10, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.rectangle(resized, (x, y), (x + w, y + h), (255, 0, 0), 2)
    dim_text = f"{w}x{h} px"
    cv2.putText(resized, dim_text, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

cv2.imshow("Filtrowane kostki", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
