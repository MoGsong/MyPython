import cv2
import numpy as np
img = cv2.imread('hzz.jpg', 1)
cv2.imshow('src',img)
#双边滤波
dst = cv2.bilateralFilter(img,15,35,35)
cv2.imshow('dst',dst)
cv2.waitKey(0)