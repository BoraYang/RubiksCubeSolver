import cv2
import numpy as np
import math
#from matplotlib import pyplot as plt

def get_average(colorValues):
  blue = 0
  green = 0
  red = 0
  listAvgTotalCount = len(colorValues)

  for bgr in colorValues:
    blue+=bgr[0]**2
    green+=bgr[1]**2
    red+=bgr[2]**2

  #returns rgb value array
  return [int(math.sqrt(red/listAvgTotalCount)),int(math.sqrt(green/listAvgTotalCount)),int(math.sqrt(blue/listAvgTotalCount))]

image = cv2.imread("farTop.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
canny = cv2.Canny(blurred, 20, 40)
kernel = np.ones((2,2), np.uint8)
dilated = cv2.dilate(canny, kernel, iterations=2)
#ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
#ret,thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
#ret,thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
#ret,thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
#ret,thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

#titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
#images = [image, thresh1, thresh2, thresh3, thresh4, thresh5]
#for i in range(6):
#    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
#plt.show()
cv2.imshow('image',dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print("Orange value average")
# orangevals = []
# orangevals.append(image[149][404])
# orangevals.append(image[154][379])
# orangevals.append(image[156][402])
# orangevals.append(image[158][428])
# orangevals.append(image[165][405])
# print(get_average(orangevals))
# print()

# print("Red value average")
# redvals = []
# redvals.append(image[190][399])
# redvals.append(image[204][355])
# redvals.append(image[202][395])
# redvals.append(image[208][433])
# redvals.append(image[221][387])
# print(get_average(redvals))
# print()

# print("White value average")
# whitevals = []
# whitevals.append(image[257][411])
# whitevals.append(image[246][456])
# whitevals.append(image[306][408])
# whitevals.append(image[278][431])
# whitevals.append(image[297][447])
# print(get_average(whitevals))
# print()

# print("Yellow value average")
# yellowvals = []
# yellowvals.append(image[322][479])
# yellowvals.append(image[306][507])
# yellowvals.append(image[358][472])
# yellowvals.append(image[336][489])
# yellowvals.append(image[350][501])
# print(get_average(yellowvals))
# print()
