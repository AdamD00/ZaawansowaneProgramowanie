import cv2

image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
(cX, cY) = w //2, h // 2

(b,g,r) = image[cX,cY]
print("Pixel at ({},{}) - Red: {}, Green: {}, Blue: {}".format(cX,cY,r, g, b))