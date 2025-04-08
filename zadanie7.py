import cv2
image = cv2.imread("example.png")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
h,s,v=cv2.split(hsv)
s_Higher= s+50
s_lower= s-50
hsv_modified = cv2.merge([h,s_Higher,v])
hsv_modified2 = cv2.merge([h,s_lower,v])
cv2.imshow("Higher S",hsv_modified)
cv2.imshow("Lower S",hsv_modified2)
cv2.waitKey(0)
cv2.destroyAllWindows()