import cv2


image = cv2.imread('stockface.jpg')
(h,w) = image.shape[:2]
blue = (255, 0,0)
red = (0, 0, 255)
green = (0,255,0)
# loop over increasing radii, from 0 pixels to 150 pixels in 25
# pixel increments
for r in range(0, 15):
    cv2.circle(image,(245,115),r, red)
    cv2.circle(image,(295,117),r, red)
cv2.rectangle(image,(245,160),(300,180),green,20)
cv2.circle(image,(w//2,h//2-50),110,blue)
cv2.imshow("Face",image)
cv2.waitKey(0)