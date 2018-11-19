import cv2
import numpy as np

image = cv2.imread("closeTop.jpg")
image = image[0:310,115:480]

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray_image,120,255,0)

im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
   # calculate moments for each contour
   M = cv2.moments(c)
 
   # calculate x,y coordinate of center
   if M["m00"] == 0:
   	cX = 0
   	cY = 0
   else:
   	cX = int(M["m10"] / M["m00"])
   	cY = int(M["m01"] / M["m00"])
   
   cv2.circle(image, (cX, cY), 5, (255, 255, 255), -1)
   cv2.putText(image, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
 
   # display the image
   cv2.imshow("Image", image)
   cv2.waitKey(0)

# cv2.imshow('image',thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()