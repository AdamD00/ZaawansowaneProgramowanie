import cv2

def nothing(x):
    pass

image_path = "example.png"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Adaptive Thresholding")


cv2.createTrackbar("blockSize", "Adaptive Thresholding", 11, 51, nothing)
cv2.createTrackbar("C", "Adaptive Thresholding", 10, 40, nothing)  # offset 20, będziemy odejmować

while True:
    blockSize = cv2.getTrackbarPos("blockSize", "Adaptive Thresholding")
    if blockSize % 2 == 0:
        blockSize += 1
    if blockSize < 3:
        blockSize = 3

    C = cv2.getTrackbarPos("C", "Adaptive Thresholding") - 20

    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, blockSize, C)

    cv2.imshow("Adaptive Thresholding", thresh)

    key = cv2.waitKey(100) & 0xFF
    if key == 27:  # ESC do wyjścia
        break

cv2.destroyAllWindows()
