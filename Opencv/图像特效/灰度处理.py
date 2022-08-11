import cv2
# img0 = cv2.imread('hzz.jpg', 0)
# img1 = cv2.imread('hzz.jpg', 1)
# print(img0.shape)
# print(img1.shape)
# cv2.imshow('src', img0)
# cv2.imshow('img', img1)
# cv2.waitKey(0)

#cvtColor
img = cv2.imread('hzz.jpg', 1)
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #颜色空间转换  1.转换图片 2.转换方法
cv2.imshow('img', dst)
cv2.waitKey(0)