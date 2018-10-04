import cv2
import numpy as np

image = cv2.imread("mixedccolors.jpg")

#for i in range(480):
 #   print('='*40)
  #  for j in range(640):
   #     print(image[i][j])
        #b,g,r = image[i][j] #Images broken into blue, green, red channels

print("Orange values\n")
print(image[149][404])
print(image[154][379])
print(image[156][402])
print(image[158][428])
print(image[165][405])

print("Red values\n")
print(image[190][399])
print(image[204][355])
print(image[202][395])
print(image[208][433])
print(image[221][387])

print("White values\n")
print(image[257][411])
print(image[246][456])
print(image[306][408])
print(image[278][431])
print(image[297][447])

print("Yellow values\n")
print(image[322][479])
print(image[306][507])
print(image[358][472])
print(image[336][489])
print(image[350][501])    


