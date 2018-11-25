import cv2
import numpy as np

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
      #print(f"HSV Value: {hsvImage[midY][midX]}")
      #rect = hsvImage[y:y+h,x:x+w]
      #v2.imshow("rect", rect)
      #print(f"Mean: {int(rect.mean())}")
      # if w > 40 or h > 6:
      #   midX = int(x+(w/2))
      #   midY = int(y+(h/2))
      #   cv2.circle(inputImage, (midX,midY), 5, (255, 255, 255), -1) #Getting center of bounding rectangle, which is center of cube face
      #   print(hsvImage[midY][midX])
      # else:
      #   continue
        
      cv2.imshow("Image", inputImage)
      cv2.waitKey(0)