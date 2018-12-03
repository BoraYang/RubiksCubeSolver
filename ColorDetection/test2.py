import cv2
import numpy as np

def setupLowMasks(hsvImage):

	tempList = []

	y = cv2.inRange(hsvImage,(26,40,100),(40,255,255))
	w = cv2.inRange(hsvImage,(0,0,50),(255,60,255))
	b = cv2.inRange(hsvImage,(100,100,0),(140,255,255))
	g = cv2.inRange(hsvImage,(41,50,35),(85,255,255))
	r = cv2.inRange(hsvImage,(0,140,20),(10,240,255))
	o = cv2.inRange(hsvImage,(5,50,50),(25,255,255))

	tempList.extend([y,w,b,g,r,o])
	return tempList

def setupTopMasks(hsvImage):

	tempList = []

	y = cv2.inRange(hsvImage,(26,40,55),(40,255,255))
	w = cv2.inRange(hsvImage,(0,0,0),(255,90,255))
	b = cv2.inRange(hsvImage,(100,80,0),(140,255,255))
	g = cv2.inRange(hsvImage,(50,50,0),(85,255,255))
	rl = cv2.inRange(hsvImage,(0,50,0),(10,255,255))
	rh = cv2.inRange(hsvImage,(160,50,0),(180,255,255))
	r = rl | rh
	o = cv2.inRange(hsvImage,(5,50,80),(25,255,255))

	tempList.extend([y,w,b,g,r,o])
	return tempList

bgr_image_ct = cv2.imread("closeTop.jpg")
bgr_image_cb = cv2.imread("closeBottom.jpg")
bgr_image_ft = cv2.imread("farTop.jpg")
bgr_image_fb = cv2.imread("farBottom.jpg")

hsv_image_ct = cv2.cvtColor(bgr_image_ct,cv2.COLOR_BGR2HSV)
hsv_image_cb = cv2.cvtColor(bgr_image_cb,cv2.COLOR_BGR2HSV)
hsv_image_ft = cv2.cvtColor(bgr_image_ft,cv2.COLOR_BGR2HSV)
hsv_image_fb = cv2.cvtColor(bgr_image_fb,cv2.COLOR_BGR2HSV)

mask_list_ct = setupTopMasks(hsv_image_ct)
mask_list_cb = setupLowMasks(hsv_image_cb)
mask_list_ft = setupTopMasks(hsv_image_ft)
mask_list_fb = setupLowMasks(hsv_image_fb)

# for i in [5,7,8,9,10,11,12,15,19,20,23,26]:

# 	xd = f"mask{str(i)}.jpg"

# 	test_image = cv2.imread(xd, cv2.IMREAD_GRAYSCALE)
# 	_, im_bw = cv2.threshold(test_image, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# 	mask_apply = cv2.bitwise_and(bgr_image_ct,bgr_image_ct,mask=im_bw)

# 	target1 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_ct[0])
# 	target2 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_ct[1])
# 	target3 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_ct[2])
# 	target4 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_ct[3])
# 	target5 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_ct[4])
# 	target6 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_ct[5])

# 	print(i)
# 	print(f"Yellow: {np.count_nonzero(target1)}")
# 	print(f"White: {np.count_nonzero(target2)}")
# 	print(f"Blue: {np.count_nonzero(target3)}")
# 	print(f"Green: {np.count_nonzero(target4)}")
# 	print(f"Red: {np.count_nonzero(target5)}")
# 	print(f"Orange: {np.count_nonzero(target6)}")

# 	cv2.imshow("Cube", mask_apply)
# 	cv2.waitKey(0)

#[18,21,24,25,27,28,29,30,33,41,42,43,44]
for i in [28,29]:

	xd = f"mask{str(i)}.jpg"

	test_image = cv2.imread(xd, cv2.IMREAD_GRAYSCALE)
	_, im_bw = cv2.threshold(test_image, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	mask_apply = cv2.bitwise_and(bgr_image_cb,bgr_image_cb,mask=im_bw)

	target1 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_cb[0])
	target2 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_cb[1])
	target3 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_cb[2])
	target4 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_cb[3])
	target5 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_cb[4])
	target6 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_cb[5])

	print(i)
	print(f"Yellow: {np.count_nonzero(target1)}")
	print(f"White: {np.count_nonzero(target2)}")
	print(f"Blue: {np.count_nonzero(target3)}")
	print(f"Green: {np.count_nonzero(target4)}")
	print(f"Red: {np.count_nonzero(target5)}")
	print(f"Orange: {np.count_nonzero(target6)}")

	cv2.imshow("green", mask_apply)
	cv2.waitKey(0)

# for i in [0,1,2,3,6,36,37,38,39,45,46,47,50,53]:

# 	xd = f"mask{str(i)}.jpg"

# 	test_image = cv2.imread(xd, cv2.IMREAD_GRAYSCALE)
# 	_, im_bw = cv2.threshold(test_image, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# 	mask_apply = cv2.bitwise_and(bgr_image_ft,bgr_image_ft,mask=im_bw)

# 	target1 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_ft[0])
# 	target2 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_ft[1])
# 	target3 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_ft[2])
# 	target4 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_ft[3])
# 	target5 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_ft[4])
# 	target6 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_ft[5])

# 	print(i)
# 	print(f"Yellow: {np.count_nonzero(target1)}")
# 	print(f"White: {np.count_nonzero(target2)}")
# 	print(f"Blue: {np.count_nonzero(target3)}")
# 	print(f"Green: {np.count_nonzero(target4)}")
# 	print(f"Red: {np.count_nonzero(target5)}")
# 	print(f"Orange: {np.count_nonzero(target6)}")

# 	cv2.imshow("Cube", mask_apply)
# 	cv2.waitKey(0)

# for i in [14,16,17,32,34,35,48,51,52]:

# 	xd = f"mask{str(i)}.jpg"

# 	test_image = cv2.imread(xd, cv2.IMREAD_GRAYSCALE)
# 	_, im_bw = cv2.threshold(test_image, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# 	mask_apply = cv2.bitwise_and(bgr_image_fb,bgr_image_fb,mask=im_bw)

# 	target1 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_fb[0])
# 	target2 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_fb[1])
# 	target3 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_fb[2])
# 	target4 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_fb[3])
# 	target5 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_fb[4])
# 	target6 = cv2.bitwise_and(mask_apply,mask_apply,mask=mask_list_fb[5])

# 	print(i)
# 	print(f"Yellow: {np.count_nonzero(target1)}")
# 	print(f"White: {np.count_nonzero(target2)}")
# 	print(f"Blue: {np.count_nonzero(target3)}")
# 	print(f"Green: {np.count_nonzero(target4)}")
# 	print(f"Red: {np.count_nonzero(target5)}")
# 	print(f"Orange: {np.count_nonzero(target6)}")

# 	cv2.imshow("Cube", mask_apply)
# 	cv2.waitKey(0)