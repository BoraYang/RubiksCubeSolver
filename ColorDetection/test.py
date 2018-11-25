import cv2
import numpy as np

bgr_image = cv2.imread("closeTop.jpg")
hsv_image = cv2.cvtColor(bgr_image,cv2.COLOR_BGR2HSV)

#White cube face
test_image = cv2.imread("mask4.jpg", cv2.IMREAD_GRAYSCALE)
_, im_bw = cv2.threshold(test_image, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
mask_apply = cv2.bitwise_and(bgr_image,bgr_image,mask=im_bw)

color_mask_list = []

#True
mask_white = cv2.inRange(hsv_image,(0,0,160),(255,50,255))
color_mask_list.append(mask_white)

#False
mask_blue = cv2.inRange(hsv_image,(100,150,0),(140,255,255))
color_mask_list.append(mask_blue)

#False
mask_green = cv2.inRange(hsv_image,(50,50,80),(85,255,255))
color_mask_list.append(mask_green)

target1 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_white)
target2 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_blue)
target3 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_green)

print(f"White Count: {np.count_nonzero(target1)}")
print(f"Blue Count: {np.count_nonzero(target2)}")
print(f"Green Count: {np.count_nonzero(target3)}")

cv2.imshow("White", target1)
cv2.imshow("Blue", target2)
cv2.imshow("Green", target3)
cv2.waitKey(0)