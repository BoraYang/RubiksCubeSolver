import cv2
import numpy as np


def blobDetection(inputImage):

    cv2.GaussianBlur(inputImage,(5,5),0)

    gray_image = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray_image,40,255,0)

    _, contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        
      # M = cv2.moments(c)

      # if M["m10"] == 0 or M["m01"] == 0:
      #   continue

      # # calculate x,y coordinate of center
      # if M["m00"] == 0:
      #   continue
      # else:
      #   cX = int(M["m10"] / M["m00"])
      #   cY = int(M["m01"] / M["m00"])

      # cv2.circle(inputImage, (cX, cY), 5, (255, 255, 255), -1)

      (x,y,w,h) = cv2.boundingRect(c)
      if w > 40 or h > 30:
          cv2.circle(inputImage, (int(x+(w/2)), int(y+(h/2))), 5, (255, 255, 255), -1) #Getting center of boudning rectangle, which is center of cube face
          #cv2.rectangle(inputImage, (x,y), (x+w,y+h), (0,255,0), 2)
      else:
          continue
        
      cv2.imshow("Image", inputImage)
      cv2.waitKey(0)

def maskImagePreprocess(inputImage,mask):

  _, im_bw = cv2.threshold(quick_mask, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
  mask_apply = cv2.bitwise_and(bgr_image,bgr_image,mask=quick_mask)

  return mask_apply

bgr_image = cv2.imread("closeTop.jpg") #[0:280,120:470]

quick_mask = cv2.imread("closeTopMask.jpg", cv2.IMREAD_GRAYSCALE) #[0:280,120:470]
quick_mask = maskImagePreprocess(bgr_image,quick_mask)

cv2.medianBlur(bgr_image,3)

hsv_image = cv2.cvtColor(bgr_image,cv2.COLOR_BGR2HSV)

mask_list = []

mask_yellow = cv2.inRange(hsv_image,(26,60,130),(36,140,190))
mask_list.append(mask_yellow)

mask_white = cv2.inRange(hsv_image,(0,0,160),(255,50,255))
mask_list.append(mask_white)

mask_blue = cv2.inRange(hsv_image,(100,150,0),(140,255,255))
mask_list.append(mask_blue)

mask_green = cv2.inRange(hsv_image,(50,50,80),(85,255,255))
mask_list.append(mask_green)

mask_red = cv2.inRange(hsv_image,(0,170,100),(10,255,160))
mask_list.append(mask_red)

mask_orange = cv2.inRange(hsv_image,(5,100,200),(25,199,255))
mask_list.append(mask_orange)

colorString = ("U"*9) + ("R"*9) + ("F"*9) + ("D"*9) + ("L"*9) + ("B"*9)
for mask in mask_list:
    target = cv2.bitwise_and(quick_mask,quick_mask,mask=mask)
    blobDetection(target)

combined_masks = mask_yellow + mask_white + mask_blue + mask_green + mask_red + mask_orange

target = cv2.bitwise_and(quick_mask,quick_mask,mask=combined_masks)

cv2.imshow('image1',target)
cv2.waitKey(0)
cv2.destroyAllWindows()