# import the necessary packages
import cv2
# load the original input image and display it to our screen
image = cv2.imread("example.jpg")
(w,h) = image.shape[:2]
LT = image[0:w//2,0:h//2]
RT = image[w//2:w,0:h//2]
LB = image[0:w//2,h//2:h]
RB = image[w//2:w,h//2:h]
RT = cv2.flip(RT,1)
LB = cv2.flip(LB,0)
RB = cv2.flip(RB,-1)
image[0:w//2,0:h//2] = LT
image[w//2:w,0:h//2] = RT
image[0:w//2,h//2:h] = LB
image[w//2:w,h//2:h] = RB
cv2.imshow("Part fliped",image)
cv2.waitKey(0)