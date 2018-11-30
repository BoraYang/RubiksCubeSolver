#TODO: Once the actual cube images are taken from each camera(1,2,3,4), the mask values (all 48 (54-6 for center pieces))
#will need to be generated in GIMP. Certain masks will use different images, so when creating the masks, make note of which image they
#correspond to. In the 'mask loop' (marked mask loop below towards the bottom) have a check with an array (e.g. i (mask index) in [1,2,3])
#for the masks that correspond to which camera's image will be used in the getCubeColor function. Will possibly need to have a light/dark
#color range for images (top/bottom are different and will need different color ranges if we dont use lights)

import cv2
import numpy as np


def getColorRanges(hsvImage, color_list):

  mask_yellow = cv2.inRange(hsvImage,(26,60,130),(36,140,190))
  color_mask_list.append(mask_yellow)

  mask_white = cv2.inRange(hsvImage,(0,0,160),(255,50,255))
  color_mask_list.append(mask_white)

  mask_blue = cv2.inRange(hsvImage,(100,120,0),(140,255,255))
  color_mask_list.append(mask_blue)

  mask_green = cv2.inRange(hsvImage,(50,50,80),(85,255,255))
  color_mask_list.append(mask_green)

  mask_red = cv2.inRange(hsvImage,(0,170,100),(10,255,160))
  color_mask_list.append(mask_red)

  mask_orange = cv2.inRange(hsvImage,(5,100,200),(25,199,255))
  color_mask_list.append(mask_orange)

def getCubeColor(cube_square, color_array, cube_string, position):
  #Position needs to be decremented by 1 to match cube_string index. Or change "mask.jpg" to start from 0.

  #Yellow: 0, White: 1, Blue: 2, Green: 3, Red: 4, Orange: 5
  #Yellow: U, White: D, Blue: L, Green: R, Red: F, Orange: B

  cv2.imshow("CS",cube_square)
  cv2.waitKey(0)

  #Determine if cube square is of a certain color. If it is a certain color, the value stored in the variable will be greater than zero.
  yellow = np.count_nonzero(cv2.bitwise_and(cube_square,cube_square,mask=color_array[0]))
  white = np.count_nonzero(cv2.bitwise_and(cube_square,cube_square,mask=color_array[1]))
  blue = np.count_nonzero(cv2.bitwise_and(cube_square,cube_square,mask=color_array[2]))
  green = np.count_nonzero(cv2.bitwise_and(cube_square,cube_square,mask=color_array[3]))
  red = np.count_nonzero(cv2.bitwise_and(cube_square,cube_square,mask=color_array[4]))
  orange = np.count_nonzero(cv2.bitwise_and(cube_square,cube_square,mask=color_array[5]))

  print(f"Y:{yellow},W:{white},B:{blue},G:{green},R:{red},O:{orange}")

  if yellow > 100:
    cube_string[position] = 'U'
    return
  if white > 100:
    cube_string[position] = 'D'
    return
  if blue > 100:
    cube_string[position] = 'L'
    return
  if green > 100:
    cube_string[position] = 'R'
    return
  if red > 100:
    cube_string[position] = 'F'
    return
  if orange > 100:
    cube_string[position] = 'B'
    return

def maskImagePreprocess(inputImage,mask):

  _, im_bw = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
  mask_apply = cv2.bitwise_and(inputImage,inputImage,mask=im_bw)

  return mask_apply

bgr_image_ct = cv2.imread("closeTop.jpg")
bgr_image_cb = cv2.imread("closeBottom.jpg")
bgr_image_ft = cv2.imread("farTop.jpg")
bgr_image_fb = cv2.imread("farBottom.jpg")

# cv2.medianBlur(bgr_image_ct,3)
# cv2.medianBlur(bgr_image_cb,3)
# cv2.medianBlur(bgr_image_ft,3)
# cv2.medianBlur(bgr_image_fb,3)


hsv_image = cv2.cvtColor(bgr_image_ct,cv2.COLOR_BGR2HSV)

color_mask_list = []
#Yellow: 0, White: 1, Blue: 2, Green: 3, Red: 4, Orange: 5
getColorRanges(hsv_image, color_mask_list)

colorString = list("U"*9) + list("R"*9) + list("F"*9) + list("D"*9) + list("L"*9) + list("B"*9)


#Mask loop
for i in range(54):

  if i in [4,13,22,31,40,49]:
    continue

  if i in [5,7,8,9,10,11,12,15,19,20,23,26]:
    bgr_image = bgr_image_ct

  if i in [18,21,24,25,27,28,29,30,33,41,42,43,44]:
    bgr_image = bgr_image_cb

  if i in [0,1,2,3,6,36,37,38,39,45,46,47,50,53]:
    bgr_image = bgr_image_ft

  if i in [14,16,17,32,34,35,48,51,52]:
    bgr_image = bgr_image_fb

  #Formats a filename string for the mask in order. Skips mask #'s that cannot be seen by the current image, or are a center piece
  cube_mask = f"mask{str(i)}.jpg"

  #Convert cube square to black/white image for erode scaling
  bw_square = cv2.imread(cube_mask, cv2.IMREAD_GRAYSCALE)

  #Erodes part of the cube square to eliminate extraneous black or white perimeter
  kernel = np.ones((5,5), np.uint8)
  erode = cv2.erode(bw_square, kernel, iterations = 2)
  cube_square = maskImagePreprocess(bgr_image,erode)

  getCubeColor(cube_square,color_mask_list,colorString,i)

finalCubeString = "".join(colorString)
print(finalCubeString)