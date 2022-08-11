import cv2
import numpy as np
#矩阵变换的方法进行矩阵缩放
img = cv2.imread('hzz.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
dst = np.zeros(img.shape, np.uint8)
height = imgInfo[0]
width = imgInfo[1]
#newX、Y = A*x+ B*y + C
matScale = np.float32([[0.5, 0, 0], [0, 0.5, 0]]) #建一个缩放矩阵
dst = cv2.warpAffine(img, matScale, (int(width/2), int(height/2)))
cv2.imshow('dst', dst)
cv2.waitKey(0)
# key = cv2.waitKey(0) & 0xff
# if key == ord('q'):
#     cv2.destroyWindow()