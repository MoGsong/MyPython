# import cv2
# import numpy as np
# img = cv2.imread('hzz.jpg',1)
# # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('src',img)
# # dst = cv2.equalizeHist(gray)
# (b,g,r) = cv2.split(img)       #通道拆分
# bH = cv2.equalizeHist(b)       #通道分别均衡化
# gH = cv2.equalizeHist(g)
# rH = cv2.equalizeHist(r)
# result = cv2.merge((bH,gH,rH))    #通道合成
# cv2.imshow('dst',result)
# cv2.waitKey(0)

#YUV
import cv2
import numpy as np
img = cv2.imread('hzz.jpg',1)
cv2.imshow('src',img)
imgYUV = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
channelYUV = cv2.split(imgYUV)
channelYUV[0] = cv2.equalizeHist(channelYUV[0])
ch = cv2.merge(channelYUV)
result = cv2.cvtColor(ch,cv2.COLOR_YCrCb2BGR)
cv2.imshow('dst',result)
cv2.waitKey(0)