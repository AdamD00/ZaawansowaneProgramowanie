import cv2
import imutils

# load the original input image and display it on our screen
image = cv2.imread("example.jpg")
cv2.imshow("Original", image)

methods = [
("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
# loop over the interpolation methods
for (name, method) in methods:
    #increase the size of the image by 3x using the current
    # interpolation method
    print("[INFO] {}".format(name))
    resized = imutils.resize(image, width=image.shape[1] * 4,
                             inter=method)
    cv2.imshow("Method: {}".format(name), resized)
cv2.waitKey(0)