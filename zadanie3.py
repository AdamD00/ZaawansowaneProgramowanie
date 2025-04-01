import cv2

gray = cv2.imread('captcha.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow("Original", gray)
kernelSizes = [(20, 1), (3, 3), (20, 3), (20,15)]
# loop over the kernels sizes
for kernelSize in kernelSizes:
    # construct a rectangular kernel from the current size and then
    # apply an "opening" operation
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernelSize)
    opening = cv2.morphologyEx(gray.copy(), cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)
cv2.waitKey(0)
