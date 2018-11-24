import cv2
import numpy as np


def getColorRanges(color_list):

  mask_yellow = cv2.inRange(hsv_image,(26,60,130),(36,140,190))
  color_mask_list.append(mask_yellow)

  mask_white = cv2.inRange(hsv_image,(0,0,160),(255,50,255))
  color_mask_list.append(mask_white)

  mask_blue = cv2.inRange(hsv_image,(100,150,0),(140,255,255))
  color_mask_list.append(mask_blue)

  mask_green = cv2.inRange(hsv_image,(50,50,80),(85,255,255))
  color_mask_list.append(mask_green)

  mask_red = cv2.inRange(hsv_image,(0,170,100),(10,255,160))
  color_mask_list.append(mask_red)

  mask_orange = cv2.inRange(hsv_image,(5,100,200),(25,199,255))
  color_mask_list.append(mask_orange)

def getCenterOfCube(hsvImage,inputImage):

    cv2.GaussianBlur(inputImage,(5,5),0)

    gray_image = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray_image,40,255,0)

    _, contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:

      (x,y,w,h) = cv2.boundingRect(c)
      midX = int(x+(w/2))
      midY = int(y+(h/2))
      cv2.circle(inputImage, (midX,midY), 5, (255, 255, 255), -1) #Getting center of boudning rectangle, which is center of cube face
      print(f"HSV Value: {hsvImage[midY][midX]}")
      rect = hsvImage[y:y+h,x:x+w]
      cv2.imshow("rect", rect)
      print(f"Mean: {int(rect.mean())}")
      # if w > 40 or h > 6:
      #   midX = int(x+(w/2))
      #   midY = int(y+(h/2))
      #   cv2.circle(inputImage, (midX,midY), 5, (255, 255, 255), -1) #Getting center of boudning rectangle, which is center of cube face
      #   print(hsvImage[midY][midX])
      # else:
      #   continue
        
      cv2.imshow("Image", inputImage)
      cv2.waitKey(0)

def maskImagePreprocess(inputImage,mask):

  _, im_bw = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
  mask_apply = cv2.bitwise_and(inputImage,inputImage,mask=im_bw)

  return mask_apply

cube_mask_list = ["mask1.jpg","mask2.jpg","mask3.jpg","mask4.jpg"]

bgr_image = cv2.imread("closeTop.jpg") #[0:280,120:470]

mask_image = cv2.imread("closeTopMask.jpg", 0) #[0:280,120:470]
mask_image = maskImagePreprocess(bgr_image,mask_image)

cv2.medianBlur(bgr_image,3)

hsv_image = cv2.cvtColor(bgr_image,cv2.COLOR_BGR2HSV)

color_mask_list = []
#Yellow: 0, White: 1, Blue: 2, Green: 3, Red: 4, Orange: 5
getColorRanges(color_mask_list)

colorString = list("U"*9) + list("R"*9) + list("F"*9) + list("D"*9) + list("L"*9) + list("B"*9)

for i in range(1,18):

  if i in [5,7,14]:
    continue

  cube_mask = f"mask{str(i)}.jpg"

  bw_square = cv2.imread(cube_mask, cv2.IMREAD_GRAYSCALE)
  kernel = np.ones((5,5), np.uint8)
  erode = cv2.erode(bw_square, kernel, iterations = 2)
  cube_sqaure = maskImagePreprocess(bgr_image,erode)

  #Assign this function call to a 'square_color' variable that will assign a color to each position in the output string
  getCenterOfCube(hsv_image,cube_sqaure)

# for mask in color_mask_list:
#     target = cv2.bitwise_and(mask_image,mask_image,mask=mask)
#     getCenterOfCube(target)

cv2.imshow('image1',bgr_image)
cv2.waitKey(0)
cv2.destroyAllWindows()