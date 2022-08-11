#运行不出来，debug有数值，无错误
import cv2
import numpy as np
# cv2.setUseOptimized(onoff=True)
img = cv2.imread('hzz.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = np.zeros((height, width, 3),np.uint8)
x = 2
for i in range(x,height-x):
    for j in range(x, width-x):
        array1 = np.zeros(2*x, np.uint8)
        # print(array1)
        for m in range(-x,x):
            for n in range(-x,x):
                p1 = int(gray[i+m,j+n]/64)
                array1[p1] = array1[p1] + 1
        currentMax = array1[0]
        l = 0
        for k in range(0,2*x):
            if currentMax < array1[k]:
                currentMax = array1[k]
                l = k
        #简化 均值
        for m in range(-x,x):
            for n in range(-x,x):
                if gray[i+m,j+n]>=(l*64) and gray[i+m,j+n]<=((l+1)*64):
                        (b,g,r) = img[i+m,j+n]
        dst[i,j] = (b,g,r)
        # print(dst[i,j])
cv2.imshow('img', img)
cv2.imshow('dst',dst)
cv2.waitKey(0)