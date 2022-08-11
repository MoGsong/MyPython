import cv2
import numpy as np
img = cv2.imread('hzz.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
dst = np.zeros(img.shape, np.uint8)
height = imgInfo[0]
width = imgInfo[1]
matSrc = np.float32([[0, 0], [0, height - 1], [width - 1, 0]])  #原来的图片的三个点确定放射变换的平面坐标矩阵
matDst = np.float32([[25, 25], [100, height - 1], [width - 100, 100]])  #要映射到的平面坐标矩阵
matAffine = cv2.getAffineTransform(matSrc, matDst)  #mat 变角坐标矩阵  映射后的矩阵位置
dst = cv2.warpAffine(img, matAffine, (width, height))
cv2.imshow('dst', dst)
cv2.waitKey(0)