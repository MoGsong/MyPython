#浮点=》定点， +-》*/，>>
import cv2
import numpy as np
img = cv2.imread('hzz.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dst = np.zeros(img.shape, np.uint8)
for i in range(0, height):
    for j in range(0, width):
        (b, g, r) = img[i, j]
        b, g, r = int(b), int(g), int(r)
        #Gray = (r*1 + g*2 + b*1)/4     #定点运算  乘以的数越大，误差越小        #r*0.299 + g*0.587 + b*0.114
        Gray = (r + (g << 1) + b) >> 2  #移位运算
        dst[i, j] = np.uint8(Gray)
cv2.imshow('dst', dst)
cv2.waitKey(0)
