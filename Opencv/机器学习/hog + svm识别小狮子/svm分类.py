# 身高体重分类 + 训练 + 预测
import cv2
import numpy as np
import matplotlib.pyplot as plt
# 准备数据
rand1 = np.array([[155,48],[159,50],[164,53],[168,56],[172,60]])
rand2 = np.array([[152,53],[156,55],[160,56],[172,64],[176,65]])
# label 0女生 1男生
label = np.array([[0],[0],[0],[0],[0],[1],[1],[1],[1],[1]])
# 处理数据
data = np.vstack((rand1, rand2))
data = np.array(data, dtype='float32')
# svm 处理的数据必须要有label 监督学习 0负样本 1正样本
svm = cv2.ml.SVM_create()   # ml 机器学习模块 SVM_create()
""":type:cv2.ml"""
# 属性设置
svm.setType(cv2.ml.SVM_C_SVC)  # svm type
svm.setKernel(cv2.ml.SVM_LINEAR)  # line
svm.setC(0.01)
# 训练
result = svm.train(data,cv2.ml.ROW_SAMPLE,label)
# 预测
pre_data = np.vstack([[167,55],[162,57]])
# 0女 1男
pre_data = np.array(pre_data,dtype='float32')
print(pre_data)
(pre_1,pre_2) = svm.predict(pre_data)
print(pre_2)
