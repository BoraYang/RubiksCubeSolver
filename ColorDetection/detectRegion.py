import cv2
import numpy as np

def blobDetection(inputImage):

    cv2.GaussianBlur(inputImage,(5,5),0)

    gray_image = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray_image,115,255,0)

    _, contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        
       M = cv2.moments(c)

       if M["m10"] == 0 or M["m01"] == 0:
        continue

       # calculate x,y coordinate of center
       if M["m00"] == 0:
        continue
       else:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

       #cv2.circle(inputImage, (cX, cY), 5, (255, 255, 255), -1)

        (x,y,w,h) = cv2.boundingRect(c)
        if w > 40 or h > 30:
            print(f"{x},{y}")
            cv2.rectangle(inputImage, (x,y), (x+w,y+h), (0,255,0), 2)
        else:
            continue
     
       cv2.imshow("Image", inputImage)
       cv2.waitKey(0)

bgr_image = cv2.imread("closeTop.jpg")[0:280,120:470]
quick_mask = cv2.imread("closeTopMask.jpg", cv2.IMREAD_GRAYSCALE)[0:280,120:470]
thresh, im_bw = cv2.threshold(quick_mask, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

pre_mask = cv2.bitwise_and(bgr_image,bgr_image,mask=im_bw)
#pre_mask = pre_mask[0:280,120:470]

cv2.medianBlur(bgr_image,5)

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

for mask in mask_list:
    target = cv2.bitwise_and(pre_mask,pre_mask,mask=mask)
    blobDetection(target)
    # cv2.imshow('image',target)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

combined_masks = mask_yellow + mask_white + mask_blue + mask_green + mask_red + mask_orange

#mask_red_and_orange = cv2.bitwise_or(mask_red,mask_orange)

target = cv2.bitwise_and(pre_mask,pre_mask,mask=combined_masks)

#cv2.imwrite("closeTop2.jpg",target)
cv2.imshow('image',target)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print("Green HSV Values:")
# print(hsv_image[80][175])
# print(hsv_image[99][207])
# print(hsv_image[129][210])

# print(hsv_image[136][430])
# print(hsv_image[143][440])

# print(hsv_image[18][394])
# print(hsv_image[30][429])

# print("White HSV Values:")
#print(hsv_image[200][282])
# print(hsv_image[61][133])
# print(hsv_image[99][158])
# print(hsv_image[53][207])
# print(hsv_image[34][234])
# print(hsv_image[195][253])
# print(hsv_image[96][407])
# print(hsv_image[135][379])
# print()

# print("Yellow HSV Values:")
# print(hsv_image[80][284])
# print(hsv_image[67][324])
# print(hsv_image[84][331])

# print(hsv_image[292][337])
# print(hsv_image[274][352])
# print(hsv_image[290][347])

# print(hsv_image[135][170])
# print(hsv_image[135][179])

# print(hsv_image[240][237])
# print(hsv_image[248][249])

# print("Red HSV Values:")
# print(hsv_image[3][357])
# print(hsv_image[219][323])
# print(hsv_image[192][348])
# print(hsv_image[273][317])
# print(hsv_image[262][337])
# print()

# print("Orange HSV Values:")
# print(hsv_image[5][231])
# print(hsv_image[26][164])
# print(hsv_image[81][273])
# print(hsv_image[81][323])
# print(hsv_image[42][335])
# print(hsv_image[41][383])