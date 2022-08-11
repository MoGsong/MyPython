#dst = src1 * a + src2*(1-a)
import cv2
import numpy as np
img0 = cv2.imread('hzz.jpg', 1)
img1 = cv2.imread('dy.jpg', 1)
print(img0.shape, img1.shape)
img0Info = img0.shape
height = img0Info[0]
width = img0Info[1]
#ROI
roiH = int(height/2)
roiW = int(width/2)
img0ROI = img0[0:roiH, 0:roiW]
img1ROI = img1[0:roiH, 0:roiW]
dst = np.zeros((roiH,roiW,3),np.uint8)
dst = cv2.addWeighted(img0ROI,0.5,img1ROI,0.5,0) #add dst = src1 * a + src2*(1-a)
dst1 = cv2.addWeighted(img0,0.5,img1,0.5,0)
cv2.imshow('dst', dst)
cv2.imshow('dst1',dst1)
cv2.waitKey(0)