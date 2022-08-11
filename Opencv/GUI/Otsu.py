# import cv2 as cv
# import numpy as np
#
# img = cv.imread('01.jpg',0)
# blur = cv.GaussianBlur(img,(5,5),0)
# # 找到归一化直方图还有累计分布函数
# hist = cv.calcHist([blur],[0],None,[256],[0,256])
# hist_norm = hist.ravel()/hist.max()
# Q = hist_norm.cumsum()
# bins = np.arange(256)
# fn_min = np.inf
# thresh = -1
# for i in range(1,256):
#     p1,p2 = np.hsplit(hist_norm,[i]) # 概率
#     q1,q2 = Q[i],Q[255]-Q[i] # 类别总和
#     b1,b2 = np.hsplit(bins,[i]) # 权重
#     # f 找到均值与方差
#     m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
#     v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
#     # 计算最小函数
#     fn = v1*q1 + v2*q2
#     if fn < fn_min:
#         fn_min = fn
#         thresh = i
# # 用 OpenCV 函数的 otsu'阈值
# ret, otsu = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# print("{} {}".format(thresh,ret) )


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('hzz.jpg',0)
# 全局阈值
ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# Otsu 阈值
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# 经过高斯滤波的 Otsu 阈值
blur = cv.GaussianBlur(img,(5,5),0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# 画出所有的图像和他们的直方图
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()
