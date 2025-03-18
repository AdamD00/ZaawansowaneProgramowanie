import cv2

img = cv2.imread("image.jpg")
print("Podaj start x oraz end x, start y oraz end y")
startx = int(input())
endx = int(input())
starty = int(input())
endy = int(input())

bottom = img[starty:endy,startx:endx]
cv2.imshow("R",bottom)
cv2.waitKey(0)