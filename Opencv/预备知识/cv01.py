import cv2
img = cv2.imread('hzz.jpg')
cv2.imshow('./hzz', img)
cv2.imwrite('hzz1.jpg', img, [cv2.IMWRITE_JPEG_CHROMA_QUALITY, 50]) #cv2.imwrite('./hzz1.jpg', img, [cv2.IMWRITE_PNG_compression,0])
#像素操作  （b,g,r） = img[100,100] \  img[1,100] = (255,0,0) 蓝色
(b, g, r) = img[100, 100]
for i in range(100):
    img[1+i, 100] = (255, 0, 0)
cv2.imshow('./hzz1.jpg', img)
cv2.waitKey(0)