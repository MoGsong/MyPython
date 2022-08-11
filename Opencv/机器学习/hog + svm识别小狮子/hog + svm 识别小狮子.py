# 样本 训练 测试 预测
# 正样本 负样本 正负所有样本尺寸要一致 多样化 1:2|3
# 获取样本 网络（爬虫爬取） 其他（视频获取样本）
# 整个过程分为7步：1、Hog参数设置    2、创建Hog    3、svm参数设置与创建    4、计算Hog    5、label    6、训练    7、预测
import cv2
import numpy as np
import matplotlib.pyplot as plt
# 1、设置 Hog参数，定义3780维的Hog特征
PosNum = 10  # 820
NegNum = 20  # 1931
winSize = (64,128)
blockSize = (16,16)
blockStride = (8,8)    # block步长
cellSize = (8,8)
nbin = 9  # 3780
#创建Hog
hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbin)
#svm参数设置与创建
svm = cv2.ml.SVM_create()
featureNum = int(((64 - 16) / 8+1)*((128-16)/8+1)*4*9) #3780
featureArray = np.zeros((PosNum+NegNum,featureNum),np.float32)
labelArray = np.zeros((PosNum+NegNum,1),np.int32)
# svm 是监督学习，学习的是图中的Hog特征
# 5、设置正负样本标签
for i in range(0,PosNum):
    fileName = 'pos1\\' + str(i) + '.jpg'          # str(i + 1)
    img = cv2.imread(fileName)
    hist = hog.compute(img, (8,8))    # 计算hog特征 3780 \ feature num
    # 将正样本中的 Hog特征装到featureArray中
    for j in range(0,featureNum):
        featureArray[i,j] = hist[j]    # featureArray中的每一行代表一个3780维的 Hog特征
    labelArray[i,0] = 1     # 正样本标签设置为 1
# 处理负样本
for i in range(0,NegNum):
    fileName = 'neg\\' + str(i) + '.jpg'   # \\windows下使用 ，mac /
    img = cv2.imread(fileName)
    hist = hog.compute(img, (8,8))    # 计算hog特征
    for j in range(featureNum):
        featureArray[i+PosNum, j] = hist[j]
    labelArray[i+PosNum, 0] = -1    # 负样本标签设置为 -1
# 属性设置
svm.setType(cv2.ml.SVM_C_SVC)  # svm type
svm.setKernel(cv2.ml.SVM_LINEAR)  # line
svm.setC(0.01)
# 6、训练
ret = svm.train(featureArray, cv2.ml.ROW_SAMPLE, labelArray)
print(ret)
# 7.检测
alpha = np.zeros((1), np.float32)
rho = svm.getDecisionFunction(0,alpha)           # 决策函数
print(rho)
print(alpha)
alphaArray = np.zeros((1,1),np.float32)    # 视为参数
supportVArray = np.zeros((1,featureNum),np.float32)  # 支持向量机的维度
resultArray = np.zeros((1,featureNum),np.float32)
alphaArray[0,0] = alpha
resultArray = -1 * alphaArray * supportVArray
print(resultArray)
# detect 检测
myDetect = np.zeros((3781),np.float32)
for i in range(0,3780):
    myDetect[i] = resultArray[0,i]
myDetect[3780] = rho[0]
# 构建hog
myHog = cv2.HOGDescriptor()
myHog.setSVMDetector(myDetect)
# load detect dst
test = cv2.imread('lion.png',1)
imageSrc = cv2.resize(test, (287, 450))
objs = myHog.detectMultiScale(imageSrc,0,(8,8),(32,32),1.05,2)   # 三维
x = int(objs[0][0][0])
y = int(objs[0][0][1])
w = int(objs[0][0][2])
h = int(objs[0][0][3])
cv2.rectangle(imageSrc,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('dst',imageSrc)
cv2.waitKey(0)
cv2.destroyAllWindows()