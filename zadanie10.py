import cv2

image = cv2.imread('image.jpg')


(b,g,r) = image[50,50]
(b2,g2,r2) = image[100,100]
print("Pixel at (50,50) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
print("Pixel at (100,100) - Red: {}, Green: {}, Blue: {}".format(r2, g2, b2))

