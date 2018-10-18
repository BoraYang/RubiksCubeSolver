import cv2
import numpy as np
import math

image = cv2.imread("mixedcolors.jpg")

def get_average(colorValues):
	blue = 0
	green = 0
	red = 0
	listAvgTotalCount = len(colorValues)

	for bgr in colorValues:
		blue+=bgr[0]**2
		green+=bgr[1]**2
		red+=bgr[2]**2

	return [int(math.sqrt(blue/listAvgTotalCount)),int(math.sqrt(green/listAvgTotalCount)),int(math.sqrt(red/listAvgTotalCount))]

print("Orange value average")
orangevals = []
orangevals.append(image[149][404])
orangevals.append(image[154][379])
orangevals.append(image[156][402])
orangevals.append(image[158][428])
orangevals.append(image[165][405])
print(get_average(orangevals))
print()

print("Red value average")
redvals = []
redvals.append(image[190][399])
redvals.append(image[204][355])
redvals.append(image[202][395])
redvals.append(image[208][433])
redvals.append(image[221][387])
print(get_average(redvals))
print()

print("White value average")
whitevals = []
whitevals.append(image[257][411])
whitevals.append(image[246][456])
whitevals.append(image[306][408])
whitevals.append(image[278][431])
whitevals.append(image[297][447])
print(get_average(whitevals))
print()

print("Yellow value average")
yellowvals = []
yellowvals.append(image[322][479])
yellowvals.append(image[306][507])
yellowvals.append(image[358][472])
yellowvals.append(image[336][489])
yellowvals.append(image[350][501])
print(get_average(yellowvals))
print()