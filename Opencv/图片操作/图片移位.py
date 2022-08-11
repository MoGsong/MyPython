import cv2
import numpy as np
img = cv2.imread('hzz.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
matShift = np.float32([[1, 0, 100], [0, 1, 100]])  #移动矩阵
#原理：2*3 -> 2*2（单位阵）(B)2*1  A(原矩阵(一个像素点)(x,y))*E（单位阵[1,0][0,1]]+B[100,200] = [x+100,y+100]
dst = cv2.warpAffine(img, matShift, (height, width)) #data mat info 图片移位warpAffine(放射变化)
cv2.imshow('dst', dst)
cv2.waitKey(0)