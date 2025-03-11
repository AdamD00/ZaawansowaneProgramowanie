import cv2

image = cv2.imread('image.jpg')
sumMax =0
iMax =0
jMax=0
(h, w) = image.shape[:2]
for i in range(h):
    for j in range(w):
        (b, g, r) = image[i,j]
        if(b+g+r)>sumMax:
            sumMax = b + g + r
            iMax = i
            jMax = j
print("Highest {} {}".format(iMax,jMax))