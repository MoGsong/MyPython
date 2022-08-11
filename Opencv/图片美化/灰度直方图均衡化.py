import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('hzz.jpg', 1)
cv2.imshow('src',img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
count = np.zeros(256,np.float)
for i in range(0,height):
    for j in range(0,width):
        pixel = gray[i,j]
        index = int(pixel)
        count[index] = count[index] + 1      #统计各像素的分布情况
for i in range(0,256):
    count[i] = count[i]/(height*width)   #每个像素的分布概率
sum1 = float(0)
# print(sum1)
for i in range(0,256):
    sum1 = sum1 + count[i]
    count[i] = sum1
# print(count)  #累积概率最后为1
map1 = np.zeros(256,np.uint16)
#计算映射表
for i in range(0,256):
    map1[i] = np.uint16(count[i]*255)
    #映射
for i in range(0,height):
    for j in range(0,width):
        pixel = gray[i,j]
        gray[i, j] = map1[pixel]
cv2.imshow('dst',gray)
# x = np.linspace(0,255,256)
# y = count
# plt.bar(x,y,0.9,alpha=1,color='b')
# plt.show()
cv2.waitKey(0)