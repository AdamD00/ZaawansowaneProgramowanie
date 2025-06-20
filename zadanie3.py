import cv2

image_path = "example.png"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

C_values = [2, 5, 10, 15]

for C in C_values:
    mean_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY, 11, C)
    gaussian_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 11, C)

    cv2.imshow(f"Mean C={C}", mean_thresh)
    cv2.imshow(f"Gaussian C={C}", gaussian_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
