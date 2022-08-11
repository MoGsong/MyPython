import cv2
import numpy as np
img = cv2.imread('dy.jpg',1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.rectangle(img,(0,0),(450,287),(0,255,0),3)
cv2.putText(img,'they are girl',(100,150),font,1,(200,100,255),2,cv2.LINE_AA)
cv2.imshow('src',img)
cv2.waitKey(0)