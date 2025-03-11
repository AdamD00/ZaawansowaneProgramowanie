import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Orginal", image)
(h, w) = image.shape[:2]
(cX, cY) = w //3, h // 3
(cX2,cY2) = cX*2,cY*2

tl = image[0:cY, 0:cX]
t = image[0:cY,cX:cX2]
tr = image[0:cY, cX2:w]
ml= image[cY:cY2,0:cX]
m = image[cY:cY2,cX:cX2]
mr = image[cY:cY2,cX2:w]
br = image[cY2:h, 0:cX]
bm = image[cY2:h,cX:cX2]
bl = image[cY2:h, cX2:w]


cv2.imshow("Updated", m)
cv2.waitKey(0)