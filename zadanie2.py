import cv2

image_path = "image.jpg"
image = cv2.imread(image_path)
scale_ratio = 300 / image.shape[1]
new_dim = (300, int(image.shape[0] * scale_ratio))
resized = cv2.resize(image, new_dim)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

modes = {
    "RETR_EXTERNAL": cv2.RETR_EXTERNAL,
    "RETR_TREE": cv2.RETR_TREE,
    "RETR_LIST": cv2.RETR_LIST,
}

for name, mode in modes.items():
    contours, hierarchy = cv2.findContours(thresh, mode, cv2.CHAIN_APPROX_SIMPLE)
    img_contours = resized.copy()
    cv2.drawContours(img_contours, contours, -1, (0, 0, 255), 2)

    cv2.imshow(f"Kontury - {name}", img_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()
