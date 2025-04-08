import cv2
image = cv2.imread("example.png")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
h,s,v=cv2.split(hsv)
s= s+30
hsv_modified = cv2.merge([h,s,v])
rgb_modified = cv2.cvtColor(hsv_modified,cv2.COLOR_HSV2RGB)
cv2.imshow("RGBFromHSV",rgb_modified)
cv2.waitKey(0)
cv2.destroyAllWindows()