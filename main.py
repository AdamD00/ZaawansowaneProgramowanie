import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# access the pixel located at x=50, y=20
(b, g, r) = image[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# update the pixel at (50, 20) and set it to red
image[20, 50] = (0, 0, 255)
(b, g, r) = image[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

cv2.imshow("Changed", image)
cv2.waitKey(0)
(h, w) = image.shape[:2]
(cX, cY) = w //2, h // 2


tl = image[0:cY, 0:cX]
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Left Corner", tl)
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)
cv2.waitKey(0)

# set the top-left corner of the original image to be green
image[0:cY, 0:cX] = (255, 0, 0)
# Show our updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)