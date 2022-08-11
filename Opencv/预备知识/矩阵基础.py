# import tensorflow as tf
# # import os
# # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#
# tf.compat.v1.disable_eager_execution()
#
# data1 = tf.compat.v1.placeholder(tf.float32)
# data2 = tf.compat.v1.placeholder(tf.float32)
# dataAdd = tf.add(data1, data2)
# with tf.compat.v1.Session() as sess:
#     print(sess.run(dataAdd, feed_dict={data1: 6, data2: 2}))
#     #feed_dict={data1: 6, data2: 2} 给参数赋值
# print('end!')

import tensorflow as tf

tf.compat.v1.disable_eager_execution()

data1 = tf.constant([[6, 6]])  #一行两列
data2 = tf.constant([[2],
                     [2]])     #两行一列
data3 = tf.constant([[3, 3]])  #一行两列
data4 = tf.constant([[1, 2],
                     [3, 4],
                     [5, 6]])   #三行两列
print(data1.shape)
print(data2.shape)
print(data3.shape)
print(data4.shape)
with tf.compat.v1.Session() as sess:
    print(sess.run(data4))
    print(sess.run(data4[0]))
    print(sess.run(data4[:, 0]))
    print(sess.run(data4[0, 0]))