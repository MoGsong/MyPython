import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
tf.compat.v1.disable_eager_execution()
date = np.linspace(1, 15, 15)
# print(date)
endPrice = np.array([  208.1472 , 209.1338 , 202.7850 , 209.6489  ,209.5717,
  209.0579  ,206.3236 , 205.4688 , 201.5761 , 204.8538,
  201.2699  ,200.9754,  209.5751 , 209.7059 , 208.0028])
beginPrice = np.array([  201.4189 , 207.9221 , 200.3571 , 206.7874 , 203.9223,
  204.2176 , 209.5949  ,208.4913 , 207.5774 , 206.5548,
  209.1574 , 206.5574  ,209.3399  ,207.4313 , 201.7119])

plt.figure()
for i in range(0, 15):
    #柱状图
    dateOne = np.zeros([2])
    dateOne[0] = i;
    dateOne[1] = i;
    priceOne = np.zeros([2])
    priceOne[0] = beginPrice[i]
    priceOne[1] = endPrice[i]
    if endPrice[i] > beginPrice[i]:
        plt.plot(dateOne, priceOne, 'r', lw=8)
    else:
        plt.plot(dateOne, priceOne, 'g', lw=8)
# plt.show()
dateNormal = np.zeros([15, 1])
priceNormal = np.zeros([15, 1])
for i in range(0,15):
    dateNormal[i, 0] = i/14.0
    priceNormal[i, 0] = endPrice[i]/210
x = tf.compat.v1.placeholder(tf.float32, [None, 1])
y = tf.compat.v1.placeholder(tf.float32, [None, 1])

w1 = tf.Variable(tf.compat.v1.random_uniform([1, 10], 0, 1))
b1 = tf.Variable(tf.zeros([1, 10]))
wb1 = tf.matmul(x, w1) + b1
layer1 = tf.nn.relu(wb1)  #激励函数

w2 = tf.Variable(tf.compat.v1.random_uniform([10, 1], 0, 1))
b2 = tf.Variable(tf.zeros([15, 1]))    #
wb2 = tf.matmul(layer1, w2) + b2
layer2 = tf.nn.relu(wb2)

loss = tf.reduce_mean(tf.square(y - layer2))  #计算标准差
train_stop = tf.compat.v1.train.GradientDescentOptimizer(0.1).minimize(loss)  #梯度下降
with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())   #变量初始化
    for i in range(0, 10000):             #终止条件 10000次
        sess.run(train_stop, feed_dict={x: dateNormal, y: priceNormal})      #训练值
    predict = sess.run(layer2, feed_dict={x: dateNormal})       #预测值
    predPrice = np.zeros([15, 1])
    for i in range(0,15):
        predPrice[i, 0] = (predict*210)[i, 0]
    plt.plot(date, predPrice, 'b', lw=1)
plt.show()
