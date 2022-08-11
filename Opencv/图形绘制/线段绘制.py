import cv2
import numpy as np
newImageInfo = (500,500,3)  #规定图像属性
dst = np.zeros(newImageInfo,np.uint8)
cv2.line(dst,(100,100),(400,400),(0,0,255),20,cv2.LINE_AA)
cv2.imshow('dst',dst)
cv2.waitKey(0)