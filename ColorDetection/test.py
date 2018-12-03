import cv2
import numpy as np

bgr_image = cv2.imread("closeBottom.jpg")
hsv_image = cv2.cvtColor(bgr_image,cv2.COLOR_BGR2HSV)

#Top values
# mask_yellow = cv2.inRange(hsv_image,(26,40,100),(40,255,255))
# mask_white = cv2.inRange(hsv_image,(0,0,80),(255,50,255))
# mask_blue = cv2.inRange(hsv_image,(100,100,0),(140,255,255))
# mask_green = cv2.inRange(hsv_image,(50,50,50),(85,255,255))
# mask_red = cv2.inRange(hsv_image,(0,140,20),(10,240,255))
# mask_orange = cv2.inRange(hsv_image,(5,50,50),(25,255,255))

#Bottom values
mask_yellow = cv2.inRange(hsv_image,(26,40,55),(40,255,255))
mask_white = cv2.inRange(hsv_image,(0,0,0),(255,90,255))
mask_blue = cv2.inRange(hsv_image,(100,80,0),(140,255,255))
mask_green = cv2.inRange(hsv_image,(40,50,0),(85,255,255))
mask_red_low = cv2.inRange(hsv_image,(0,50,0),(10,255,255))
mask_red_high = cv2.inRange(hsv_image,(160,50,0),(180,255,255))
mask_red = mask_red_low | mask_red_high
mask_orange = cv2.inRange(hsv_image,(5,50,80),(25,255,255))

target1 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_yellow)
target2 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_white)
target3 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_blue)
target4 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_green)
target5 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_red)
target6 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_orange)

# print(f"Red: {np.count_nonzero(target5)}")
# print(f"Orange: {np.count_nonzero(target6)}")

# cv2.imshow("Yellow", target1)
# cv2.imshow("White", target2)
# cv2.imshow("Blue", target3)
cv2.imshow("Green", target4)
# cv2.imshow("Red", target5)
# cv2.imshow("Orange", target6)
cv2.waitKey(0)

# for i in [14,16,17,32,34,35,48,51,52]:

# 	xd = f"mask{str(i)}.jpg"

# 	test_image = cv2.imread(xd, cv2.IMREAD_GRAYSCALE)
# 	_, im_bw = cv2.threshold(test_image, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# 	mask_apply = cv2.bitwise_and(bgr_image,bgr_image,mask=im_bw)

# 	target1 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_yellow)
# 	target2 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_white)
# 	target3 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_blue)
# 	target4 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_green)
# 	target5 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_red)
# 	target6 = cv2.bitwise_and(bgr_image,bgr_image,mask=mask_orange)

# 	# print(f"Yellow: {np.count_nonzero(target1)}")
# 	# print(f"White: {np.count_nonzero(target2)}")
# 	# print(f"Blue: {np.count_nonzero(target3)}")
# 	# print(f"Green: {np.count_nonzero(target4)}")
# 	# print(f"Red: {np.count_nonzero(target5)}")
# 	# print(f"Orange: {np.count_nonzero(target6)}")

# 	cv2.imshow("Masked image", target1)
# 	cv2.waitKey(0)