# import cv2
# img1=cv2.imread('1.png')
# img2=cv2.imread('2.png')
# #使用SIFT算法获取图像特征的关键点和描述符
# sift=cv2.xfeatures2d.SIFT_create()
# kp1,des1=sift.detectAndCompute(img1,None)
# kp2,des2=sift.detectAndCompute(img2,None)
#
# #定义FLANN匹配器
# indexParams=dict(algorithm=0,trees=10)
# searchParams=dict(checks=50)
# flann=cv2.FlannBasedMatcher(indexParams,searchParams)
# #使用KNN算法实现图像匹配，并对匹配结果排序
# matches=flann.knnMatch(des1,des2,k=2)
# matches=sorted(matches,key=lambda x:x[0].distance)
#
# #去除错误匹配，0.5是系数，系数大小不同，匹配的结果页不同
# goodMatches=[]
# for m,n in matches:
#     if m.distance<0.5*n.distance:
#         goodMatches.append(m)
#
# #获取某个点的坐标位置
# #index是获取匹配结果的中位数
# index=int(len(goodMatches)/2)
# #queryIdx是目标图像的描述符索引
# x,y=kp1[goodMatches[index].queryIdx].pt
# #将坐标位置勾画在2.png图片上，并显示
# cv2.rectangle(img1,(int(x),int(y)),int(x)+5,int(y)+5),(0,255,0),2)
# cv2.imshow('baofeng',img1)
# cv2.waitKey()
import cv2
import numpy as np
img = cv2.imread("01.jpg",1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]
#放大 缩放 比例
dstHeight = int(height*0.5)
dstWidth = int(width*0.5)
dst = cv2.resize(img, (dstWidth, dstHeight))   #重设尺寸--缩放
def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        print (xy)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,  1.0, (0,0,0), thickness = 1)
        cv2.imshow("image", dst)
cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
# cv2.imshow("image", img)
cv2.imshow("image", dst)
while(True):
    try:
        cv2.waitKey(100)
    except Exception:
        cv2.destroyWindow("image")
        break
cv2.waitKey(0)
cv2.destroyAllWindow()
