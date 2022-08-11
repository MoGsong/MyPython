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
index = 0
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_face = gray[y:y+h,x:x+w]            #人脸范围
    roi_color_face = img[y:y+h, x:x+w]
    fileName = str(index) + '.jpg'
    cv2.imwrite(fileName, roi_color_face)
    index = 1 + index
    eyes = eye_xml.detectMultiScale(roi_face,3)
    print('eye=', len(eyes))
    # for (e_x,e_y,e_w,e_h) in eyes:
    #     cv2.rectangle(roi_color_face,(e_x,e_y),(e_x+e_w,e_y+e_h),(0,255,0),2)
cv2.imshow('dst', img)
cv2.waitKey(0)