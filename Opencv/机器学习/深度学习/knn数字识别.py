# knn - 最近领域法
# 1.load data
# 2.calc test and train distance  zong = 5*500
# 3.knn 找到k个最近图图片5 500 1-》500train （4）
# 4.K个图片对应的内容 label标签鉴别
# 5.将label转为具体得数字
# 6.检测概率得统计
import tensorflow as tf
import numpy as np
# import random
from tensorflow.examples.tutorials.mnist import input_data
tf.compat.v1.disable_eager_execution()
# load data
mnist = input_data.read_data_sets('MINIST_data', one_hot=True)
trainNum = 55000
testNum = 10000
trainSize = 5000
testSize = 5
# data分解   replace=False不可重复
trainIndex = np.random.choice(trainNum, trainSize, replace=False)    # trainNum 张 图片中选 trainSize
testIndex = np.random.choice(testNum, testSize, replace=False)      # Num 张 图片中选 size 张 train
# 从mnist导入对应的train和test图片和label
# train
trainData = mnist.train.images[trainIndex]   # 训练图片  (500,784)
trainLabel = mnist.train.labels[trainIndex]  # label    (500,10)
# test
testData = mnist.test.images[testIndex]             # (5,784)
testLabel = mnist.test.labels[testIndex]            #  (5,10)  10 : 0 - 9 的标签
# print('GPU',tf.config.list_physical_devices())
# 28*28 = 784 图片像素
print('trainDate.shape =', trainData.shape)
print('trainLabel.shape =', trainLabel.shape)
print('testDate.shape =', testData.shape)
print('testLabel.shape =', testLabel.shape)
print(testLabel)       # 5张标签图片表示的数字 验证识别结果准确度
# 数据加载 用占位符开辟数据的空间 便于在session.run()训练中填充训练和测试得数据
trainDataInput = tf.compat.v1.placeholder(shape=[None, 784], dtype=tf.float32)    # 一个784维度 代表一张完整图片
trainLabelInput = tf.compat.v1.placeholder(shape=[None, 10], dtype=tf.float32)
testDataInput = tf.compat.v1.placeholder(shape=[None, 784], dtype=tf.float32)    # 一个784维度 代表一张完整图片
testLabelInput = tf.compat.v1.placeholder(shape=[None, 10], dtype=tf.float32)
# knn distance 5*784 -> 5*1*784
f1 = tf.expand_dims(testDataInput, 1)    # 维度扩张 便于计算
f2 = tf.subtract(trainDataInput, f1)       # 数据相减 得距离
f3 = tf.compat.v1.reduce_sum(tf.abs(f2), reduction_indices=2)  # 数据abs累加  5*500
f4 = tf.negative(f3)  # f3 取反 -》f4
f5, f6 = tf.nn.top_k(f4, k=4)   # 选取f4中最大的值 ，也是f3中最小得值 4个
# p6 is index->trainLabelInput
# get label
f7 = tf.gather(trainLabelInput, f6)
# label -> digital   reduce_sum -> reduction_indices=1 竖直上得累加
f8 = tf.compat.v1.reduce_sum(f7, reduction_indices=1)
# p9是p8中最大元素得下标 -》 5张图片中的5个数
f9 = tf.compat.v1.argmax(f8, dimension=1)

with tf.compat.v1.Session() as sess:
    #  f1 <- testData 5
    p1 = sess.run(f1, feed_dict={testDataInput: testData[0:5]})
    print('p1=', p1.shape)  # p1 (5,1,784)
    p2 = sess.run(f2, feed_dict={trainDataInput: trainData, testDataInput: testData[0:5]})   # train and test data
    print('p2=', p2.shape)   # p2= (5, 500, 784)  distance
    p3 = sess.run(f3,feed_dict={trainDataInput: trainData, testDataInput: testData[0:5]})
    print('p3=', p3.shape)   # p3= (5, 500)
    print('p3[0,0]=', p3[0,0])  # 第一张测试与第一张训练图片得距离 p3[0,0] = 150.30981

    p4 = sess.run(f4,feed_dict={trainDataInput: trainData, testDataInput: testData[0:5]})
    print('p4=', p4.shape)   # 5 50
    print('p4[0,0]=', p4[0, 0])  # p3[0,0]= 82.90586 p4[0,0]= -82.90586 # 每次运行结果不同是因为采用random 14 15行
    # p5 每一场测试图片（5）分别对应的四张最近训练图片
    p5, p6 = sess.run((f5,f6),feed_dict={trainDataInput: trainData, testDataInput: testData[0:5]})
    print('p5.shape=', p5.shape)
    print('p6.shape=', p6.shape)
    print('p5[0]', p5[0])       # p5 is distance
    print('p6[0]', p6[0])       # p6 is index
    p7 = sess.run(f7, feed_dict={trainDataInput: trainData, testDataInput: testData[0:5],trainLabelInput: trainLabel})
    print('p7.shape =', p7.shape)  # p7 = (5, 4, 10)
    print('p7[]=', p7)
    p8 = sess.run(f8, feed_dict={trainDataInput: trainData, testDataInput: testData[0:5],trainLabelInput: trainLabel})
    print('p8.shape =', p8.shape)    # p8.shape = (5, 10)
    print('p8[]=', p8)
    p9 = sess.run(f9,feed_dict={trainDataInput: trainData, testDataInput: testData[0:5],trainLabelInput: trainLabel})
    print('p9.shape =', p9.shape)  # p8.shape = (5,)
    print('p9[]=', p9)             # p9[]= [5 1 9 0 1]  # p9是p8中最大元素得下标
    # 检测二概率
    p10 = np.argmax(testLabel[0:5], axis=1)
    print('p10[]=', p10)
# 检测概率
j = 0
for i in range(0,5):
    if p9[i] == p10[i]:
        j = j+1
print('ac=', j*100/5)
