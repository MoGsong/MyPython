import numpy as np
import cv2
img = cv2.imread('01.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]
img1 = img[1390:1470, :]
# img2 = img[520:600, :]
img[520:600, :] = img1
# dstHeight = int(height*0.5)
# dstWidth = int(width*0.5)
# dst = cv2.resize(img, (dstWidth, dstHeight))
cv2.imwrite('201912700243 莫桂生.jpg', img)
cv2.imshow('0', img)
# cv2.imshow('1', img2)
cv2.waitKey(0)

