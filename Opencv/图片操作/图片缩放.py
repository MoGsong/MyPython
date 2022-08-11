import cv2
img = cv2.imread('hzz.jpg', 1)
imgInfo = img.shape
print(imgInfo)  #获得图片尺寸
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]
#放大 缩放 比例
dstHeight = int(height*0.5)
dstWidth = int(width*0.5)
dst = cv2.resize(img, (dstWidth, dstHeight))   #重设尺寸--缩放
cv2.imshow('image', dst)
cv2.waitKey(0)

#双线性插值法： A = 20%上（） + 80%下（）   B=30%左（）  +  70%右（）