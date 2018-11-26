#TODO: Once the actual cube images are taken from each camera(1,2,3,4), the mask values (all 48 (54-6 for center pieces))
#will need to be generated in GIMP. Certain masks will use different images, so when creating the masks, make note of which image they
#correspond to. In the 'mask loop' (marked mask loop below towards the bottom) have a check with an array (e.g. i (mask index) in [1,2,3])
#for the masks that correspond to which camera's image will be used in the getCubeColor function. Will possibly need to have a light/dark
#color range for images (top/bottom are different and will need different color ranges if we dont use lights)

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

def getCubeColor(cube_sqaure, color_array, cube_string, position):
  #Position needs to be decremented by 1 to match cube_string index. Or change "mask.jpg" to start from 0.

  #Yellow: 0, White: 1, Blue: 2, Green: 3, Red: 4, Orange: 5
  #Yellow: U, White: D, Blue: L, Green: R, Red: F, Orange: B

  #Determine if cube square is of a certain color. If it is a certain color, the value stored in the variable will be greater than zero.
  yellow = np.count_nonzero(cv2.bitwise_and(cube_sqaure,cube_sqaure,mask=color_array[0]))
  white = np.count_nonzero(cv2.bitwise_and(cube_sqaure,cube_sqaure,mask=color_array[1]))
  blue = np.count_nonzero(cv2.bitwise_and(cube_sqaure,cube_sqaure,mask=color_array[2]))
  green = np.count_nonzero(cv2.bitwise_and(cube_sqaure,cube_sqaure,mask=color_array[3]))
  red = np.count_nonzero(cv2.bitwise_and(cube_sqaure,cube_sqaure,mask=color_array[4]))
  orange = np.count_nonzero(cv2.bitwise_and(cube_sqaure,cube_sqaure,mask=color_array[5]))

  #print(f"Y:{yellow},W:{white},B:{blue},G:{green},R:{red},O:{orange}")

  if yellow > 100:
    cube_string[position-1] = 'U'
    return
  if white > 100:
    cube_string[position-1] = 'D'
    return
  if blue > 100:
    cube_string[position-1] = 'L'
    return
  if green > 100:
    cube_string[position-1] = 'R'
    return
  if red > 100:
    cube_string[position-1] = 'F'
    return
  if orange > 100:
    cube_string[position-1] = 'B'
    return

def maskImagePreprocess(inputImage,mask):

  _, im_bw = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
  mask_apply = cv2.bitwise_and(inputImage,inputImage,mask=im_bw)

  return mask_apply

bgr_image = cv2.imread("closeTop.jpg") #[0:280,120:470]

mask_image = cv2.imread("closeTopMask.jpg", 0) #[0:280,120:470]
mask_image = maskImagePreprocess(bgr_image,mask_image)

cv2.medianBlur(bgr_image,3)

hsv_image = cv2.cvtColor(bgr_image,cv2.COLOR_BGR2HSV)

color_mask_list = []
#Yellow: 0, White: 1, Blue: 2, Green: 3, Red: 4, Orange: 5
getColorRanges(color_mask_list)

colorString = list("U"*9) + list("R"*9) + list("F"*9) + list("D"*9) + list("L"*9) + list("B"*9)


#Mask loop
for i in range(1,18):

  if i in [5,7,14]:
    continue

  #Formats a filename string for the mask in order. Skips mask #'s that cannot be seen by the current image, or are a center piece
  cube_mask = f"mask{str(i)}.jpg" 

  #Convert cube square to black/white image for erode scaling
  bw_square = cv2.imread(cube_mask, cv2.IMREAD_GRAYSCALE)

  #Erodes part of the cube square to eliminate extraneous black or white perimeter
  kernel = np.ones((5,5), np.uint8)
  erode = cv2.erode(bw_square, kernel, iterations = 2)
  cube_square = maskImagePreprocess(bgr_image,erode)

  getCubeColor(cube_square,color_mask_list,colorString,i)

  #Assign this function call to a 'square_color' variable that will assign a color to each position in the output string
  #getCenterOfCube(hsv_image,cube_square)

finalCubeString = "".join(colorString)
print(finalCubeString)