import cv2
import numpy as np

image = cv2.imread("green.jpg")
print(image.shape)
print(image.size)


for i in range(480):
    print('='*20)
    for j in range(640):
        print(image[i][j])
        #r,g,b = image[i][j]
        
    

