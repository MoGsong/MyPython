import cv2
img = cv2.imread('image1.jpg')
imgInfo = img.shape
size =(imgInfo[1],imgInfo[0])
print(size)
VideoWrite = cv2.VideoWriter('0.mp4',-1,5,size) #写入对象 filename 编码器 帧率 size
for i in range(1,11):
    filename = 'image' + str(i) + '.jpg'
    img = cv2.imread(filename)
    VideoWrite.write(img)
print('end!')