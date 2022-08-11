import cv2
import numpy as np
import os
PosNum = 10
Infos = []
NewImg = []

def Alter_pic(img, h, w):
    ht = int(450)
    wh = int(287)
    x = int(ht / h)
    b1 = ht % h
    y = int(wh / w)
    b2 = wh % w
    if (ht == (h*x + b1)) and (wh == (w*y + b2)):
        dst = cv2.resize(img, (ht, wh))
        #dstImage = np.zeros((ht, wh, 3), np.uint8)  # 创建一个空白模板 0~255
        # matSrc = np.float32([[0, 0], [0, h - 1], [w - 1, 0]])  # 原来的图片的三个点确定放射变换的平面坐标矩阵
        # matDst = np.float32([[0, 0], [0, ht - 1], [0, wh-1]])  # 要映射到的平面坐标矩阵
        # matAffine = cv2.getAffineTransform(matSrc, matDst)  # mat 变角坐标矩阵  映射后的矩阵位置
        # dst = cv2.warpAffine(img, matAffine, (wh, ht))
    return dst

def save_pic(img=[]):
    i = 0
    if os.path.exists('./pos1'):
        os.mkdir('./pos1')
    else:
        open('pos1', 'w')
        for dst in NewImg:
            cv2.imwrite('%s' % str(i) + '.jpg', dst)
            i = i + 1
            if i == 9:
                i = 0


for i in range(0,PosNum):
    fileName = 'pos\\' + str(i) + '.png'          # str(i + 1)
    img = cv2.imread(fileName)
    imgInfo = img.shape
    print('第 %s 张图片的尺寸是 %s ' % (str(i + 1), str(imgInfo)))
    Infos.append(imgInfo)
    try:
        dst = Alter_pic(img, imgInfo[0], imgInfo[1])
        NewImg.append(dst)
        print('修改成功')
    except Exception as e:
        print('修改图片失败', e)
print(Infos)
save_pic(NewImg)
print(NewImg)


