import cv2
import numpy as np

image = cv2.imread("green.jpg")

for i in range(480):
    print('='*40)
    for j in range(640):
        print(image[i][j])
        #b,g,r = image[i][j] #Images broken into blue, green, red channels
        
    

