import cv2
import numpy as np
newImageInfo = (500,500,3)
#规定图像属性
dst = np.zeros(newImageInfo,np.uint8)
cv2.rectangle(dst,(5,100),(200,300),(255,0,0),-1)
#-1表示填充图形
cv2.circle(dst,(250,250),(50),(255,0),2)
cv2.ellipse(dst,(256,256),(150,100),0,0,180,(255,255,0),-1)
points = np.array([[15,50],[140,140],[200,170],[250,250],[15,150]],np.int32)
points = points.reshape(-1,1,2)
cv2.polylines(dst,[points],True,(0,255,255))
cv2.imshow('dst',dst)
cv2.waitKey(0)