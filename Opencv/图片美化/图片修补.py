#手动制作一张损坏图片
# import cv2
# import numpy as np
# img = cv2.imread('hzz.jpg',1)
# for i in range(100,200):
#     img[i,100] = (255,255,255)
#     img[i,100+1] = (255,255,255)
#     img[i, 100-1] = (255, 255, 255)
# for i in range(50,150):
#     img[150,i] = (255,255,255)
#     img[150, i+1] = (255, 255, 255)
#     img[150, i-1] = (255, 255, 255)
# cv2.imwrite('damage.jpg',img)
# cv2.imshow('image',img)
# cv2.waitKey(0)
import cv2
import numpy as np
img = cv2.imread('damage.jpg',1)
cv2.imshow('src',img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
paint = np.zeros((height,width,1),np.uint8)
#找出瑕疵，损坏部分
for i in range(100,200):
    paint[i,100] = 255
    paint[i,100+1] = 255
    paint[i, 100-1] = 255
for i in range(50,150):
    paint[150,i] = 255
    paint[150, i+1] = 255
    paint[150, i-1] = 255
cv2.imshow('paint',paint)
#inpaint 方法去瑕疵
imgDst = cv2.inpaint(img,paint,3,cv2.INPAINT_TELEA)
#展示结果
cv2.imshow('image',imgDst)
cv2.waitKey(0)