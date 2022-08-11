import cv2
import numpy as np
img = cv2.imread('hzz.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
dst = np.zeros(img.shape, np.uint8)
height = imgInfo[0]
width = imgInfo[1]
matRotate = cv2.getRotationMatrix2D((height*0.5, width*0.5), 45, 0.7)  #得到一个旋转矩阵 参数1.中心点 2.旋转角度 3.缩放系数
dst = cv2.warpAffine(img, matRotate, (height, width))
cv2.imshow('dst', dst)
cv2.waitKey(0)
