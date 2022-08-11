# 1.特征 = 像素经过运算后得到的解果》》可以是具体值，向量，矩阵，多维
# 利用特征识别目标   阈值判决
# 通过机器学习得到判决门限
# 特征= （p1 -p2 -p3 +p4)*w

# adaboost 分类器 把每次错误的结果特征加强
# 两级分类的阈值判断进行识别 多个分类器级联可作为一个强分类器 x1>t1 and x2>t2 and x3>t3 -》目标
# 强分类器由多个弱分类器组成，弱分类器负责计算阈值，弱分类器由若干个Node特征，一个Node有三个haar
# haar  node > nodet1 z1 = a1  haar  node < nodet1 z1 = a2
# Z =sum(z1 , z1 ,,,)>T y1 = AA   Z =sum(z1 , z1 ,,,)<T y1 = BB

# adaboost 训练
# 1.初始化权值分布
# 2.遍历阈值 p(min)
# 3.G1(x)
# 4.更新训练数据的权重分布
# 训练终止条件
import cv2
import numpy as np
# 1.load xml 2.load jpg 3.haar gray 4.detect 5.draw
face_xml = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_xml = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('BG.jpg')
cv2.imshow('src', img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_xml.detectMultiScale(gray, 1.2, 5)
# detect faces  1.data 2.scale 3,5目标像素大小，人脸不小于5
print('face=', len(faces))
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_face = gray[y:y+h,x:x+w]            #人脸范围
    roi_color_face = img[y:y+h,x:x+w]
    eyes = eye_xml.detectMultiScale(roi_face,3)
    print('eye=',len(eyes))
    for (e_x,e_y,e_w,e_h) in eyes:
        cv2.rectangle(roi_color_face,(e_x,e_y),(e_x+e_w,e_y+e_h),(0,255,0),2)
cv2.imshow('dst',img)
cv2.waitKey(0)