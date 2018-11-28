import cv2
import numpy as np

bgr_image = cv2.imread("closeTop.jpg")
hsv_image = cv2.cvtColor(bgr_image,cv2.COLOR_BGR2HSV)

#White cube face
test_image = cv2.imread("mask4.jpg", cv2.IMREAD_GRAYSCALE)
_, im_bw = cv2.threshold(test_image, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
mask_apply = cv2.bitwise_and(bgr_image,bgr_image,mask=im_bw)

mask_yellow = cv2.inRange(hsv_image,(26,30,150),(40,255,255))

mask_white = cv2.inRange(hsv_image,(0,0,100),(255,29,255))

mask_blue = cv2.inRange(hsv_image,(100,100,0),(140,255,255))

mask_green = cv2.inRange(hsv_image,(50,50,50),(85,255,255))

mask_red = cv2.inRange(hsv_image,(0,140,20),(10,240,255))

mask_orange = cv2.inRange(hsv_image,(5,100,20),(25,255,255))

target1 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_yellow)
target2 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_white)
target3 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_blue)
target4 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_green)
target5 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_red)
target6 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_orange)

print(f"Red: {np.count_nonzero(target5)}")
print(f"Orange: {np.count_nonzero(target6)}")

# cv2.imshow("Yellow", target1)
# cv2.imshow("White", target2)
# cv2.imshow("Blue", target3)
# cv2.imshow("Green", target4)
cv2.imshow("Red", target5)
cv2.imshow("Orange", target6)
cv2.waitKey(0)