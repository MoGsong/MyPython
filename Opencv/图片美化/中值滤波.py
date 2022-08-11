#代码正确，结果不对
import cv2
import numpy as np
img = cv2.imread('dy.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('src',img)
dst = np.zeros((height,width,3),np.uint8)
collect = np .zeros(9,np.uint8)
for i in range(1,height-1):
    for j in range(1,width-1):
        k = 0
        for m in range(-1,2):
            for n in range(-1,2):
                collect[k] = img[i+m,i+n]
                k = k+1
        #排序算法 冒泡比较法
        for k in range(0,9):
            p = collect[k]
            for t in range(k+1,9):
                if p < collect[t]:
                    mid = collect[t]
                    collect[t] = p
                    p = mid
        dst[i,j] = collect[4]
cv2.imshow('dst', dst)
cv2.waitKey(0)