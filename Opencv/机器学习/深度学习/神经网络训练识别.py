# "某个人脸识别"
# 1.数据加载yale 2.train label 3.cnn 4.检测
# Yale_64x64.mat
#数据准备
import cv2
#准备由训练训练数据集和测试数据集
#实现cnn数据图标检测
#使用检测数据进行检测

#模块引入,其中scipy.io是为了引入同文件夹下的数据集
import tensorflow as tf
import numpy as np
#注意加载此包
import scipy.io as sio
tf.compat.v1.disable_eager_execution()
#打开文件数据，第一个参数传递是文件名称，f是文件句柄
f =open('Yale_64x64.mat', 'rb')
#通过sio方法进行加载，加载后是字典类型
mdict = sio.loadmat(f)

#获取训练数据和训练标签
train_data = mdict['fea']
train_label = mdict['gnd']

#实现数据的无序排列
train_data = np.random.permutation(train_data)
train_label = np.random.permutation(train_label)
#从数据中抽取一部分作为测试数据
test_data = train_data[0:64]
test_label = train_label[0:64]
#生成随机种子
np.random.seed(100)
test_data = np.random.permutation(test_data)
test_label = np.random.permutation(test_label)

#准备训练数据,转换类型，对读入图片进行归一化处理，astype转换数据类型,/255是进行归一化，即像素0-1之间的转化
#转换完后，train_data数据集为三维，图片数量*64*64，其中64*64为每张图片矩阵的维度，1代表图片是黑白的
train_data = train_data.reshape(train_data.shape[0],64,64,1).astype(np.float32)/255
#数据集共有15种人脸，所以建立165*15的数据标签
train_labels_new = np.zeros((165, 15))

for i in range(0,165):
    #数据标签放在0开始的14列的标签中
    j = int(train_label[i,0]) -1
    train_labels_new[i,j] = 1
#完成训练数据的准备

test_data_input = test_data.reshape(test_data.shape[0],64,64,1).astype(np.float32)/255
test_labels_input = np.zeros((64,15))

for i in range(0,64):
    #数据标签放在0开始的14列的标签中
    j = int(test_label[i,0]) -1
    test_labels_input[i,j] = 1
#完成测试数据的准备

data_input = tf.compat.v1.placeholder(tf.float32,[None, 64, 64, 1])
label_input = tf.compat.v1.placeholder(tf.float32,[None,15])

#实现CNN卷积神经网络，并测试最终训练样本实现的检测概率
#tf.layer方法可以直接实现一个卷积神经网络的搭建
#通过卷积方法实现
layer1 = tf.compat.v1.layers.conv2d(inputs=data_input, filters = 32,kernel_size=2,
                          strides=1,padding='SAME',activation=tf.nn.relu)
#实现池化层，减少数据量，pool_size=2表示数据量减少一半
layer1_pool = tf.compat.v1.layers.max_pooling2d(layer1,pool_size=2,strides=2)
#第二层设置输出，完成维度的转换，以第一次输出作为输入，建立n行的32*32*32输出
layer2 = tf.reshape(layer1_pool,[-1,32*32*32])
#设置输出激励函数
layer2_relu = tf.compat.v1.layers.dense(layer2, 1024, tf.nn.relu)
#完成输出，设置输入数据和输出维度
output = tf.compat.v1.layers.dense(layer2_relu, 15)

#建立损失函数
loss = tf.compat.v1.losses.softmax_cross_entropy(onehot_labels=label_input,logits=output)
#使用梯度下降法进行训练
train = tf.compat.v1.train.GradientDescentOptimizer(0.01).minimize(loss)
#定义检测概率
accuracy = tf.compat.v1.metrics.accuracy(labels=tf.compat.v1.arg_max(label_input, 1),
                                         predictions=tf.compat.v1.arg_max(output, 1))[1]

#对所有变量进行初始化
init = tf.group(tf.compat.v1.global_variables_initializer(),tf.compat.v1.local_variables_initializer(),tf.compat.v1.local_variables_initializer())
#定义for循环，完成样本的加载和数据训练
with tf.compat.v1.Session() as sess:
    sess.run(init)
    for i in range(0, 200):
        #准备数据
        train_data_input = np.array(train_data)
        train_label_input = np.array(train_labels_new)
        #完成数据加载并计算损失函数和训练值
        sess.run([train,loss],feed_dict={data_input:train_data_input,label_input:train_label})
        acc = sess.run(accuracy,feed_dict={data_input:test_data_input,label_input:test_labels_input})
#打印当前概率精度
    print('acc:%.2f',acc)
