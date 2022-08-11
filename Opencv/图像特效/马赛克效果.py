#原理：一个颜色来替换矩形范围内的所有像素
import cv2
import numpy as np
img = cv2.imread('hzz.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
for m in range(100, 200):
    for n in range(100, 150):
        if m%10 == 0 and n%10 == 0:
            for i in range(0, 10):
                for j in range(0, 10):
                    (b,g,r) = img[m,n]
                    img[m + i, n + j] = (b,g,r)   #(b,g,r) = img[m,n]的颜色填充到10*10的img[m + i, n + j]方框中
cv2.imshow('img',img)
cv2.waitKey(0)