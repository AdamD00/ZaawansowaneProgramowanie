import cv2

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]
cX= input()
cY = input()
cX= int(cX)
cY = int(cY)
if cX>=0 and cX<w and cY>=0 and cY<h:
    (b,g,r) = image[cY,cX]
    print("Pixel at ({},{}) - Red: {}, Green: {}, Blue: {}".format(cX,cY,r, g, b))
else:
    print("Poza kresem")