# import cv2
# import numpy as np
# img = cv2.imread('hzz.jpg', 1)
# cv2.imshow('src',img)
# dst = cv2.GaussianBlur(img,(5,5),1.5)
# #过滤椒盐噪声 图片模糊
# cv2.imshow('dst',dst)
# cv2.waitKey(0)

#均值滤波
import cv2
import numpy as np
img = cv2.imread('hzz.jpg', 1)
cv2.imshow('src',img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dst = np.zeros((height,width,3),np.uint8)
for i in range(3,height-3):
    for j in range(3,width-3):
        sum_b = int(0)
        sum_g = int(0)
        sum_r = int(0)
        for m in range(-3,3):
            for n in range(-3,3):
                (b,g,r) = img[i+m,j+n]
                sum_b = sum_b + int(b)
                sum_g = sum_g + int(g)
                sum_r = sum_r + int(r)
        b = np.uint8(sum_b/36)
        g = np.uint8(sum_g / 36)
        r = np.uint8(sum_r / 36)
        dst[i,j] = (b,g,r)
cv2.imshow('dst',dst)
cv2.waitKey(0)
