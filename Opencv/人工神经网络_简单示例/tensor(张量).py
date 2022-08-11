import tensorflow as tf
# con_1 = tf.constant(3.0)
# con_2 = tf.constant([1,2,3,4])
# con_3 = tf.constant([[1,2],[3,4]])
# print(con_1.shape,con_2.shape,con_3.shape) #shape 维度或阶

#创建张量 与matlab创建数组方式相似 tf.placeholder
# a = tf.zeros([3,4])
# a.eval()
# b = tf.random([2,2])
# b.eval()
# #变换
# a = tf.cast(a,tf.int32)
# a = tf.reshape(a,[4,3])

#静态形状
# a.set_shape([2,3])

#变量OP 存储持久化 可修改，可训练
# a = tf.Variable(initial_value=30.0)    #tf.Variable(initial_value=None,trainable=Ture,collections=None,name=None)
# b = tf.Variable(initial_value=40.0)
# sum = tf.add(a,b)
#
#
# with tf.Session() as sess:
#     sess.run(tf.global_variable_initializer())
#     print(sess.run(sum))

#线性回归实现
import os
tf.compat.v1.disable_eager_execution()
def linear_regress():
    '''
    实现线性回归
    :return:
    '''
    with tf.variable_creator_scope("original_data"):
        X = tf.random.normal([100, 1], mean=0.0, stddev=1.0, name="original_data")
        y_ture = tf.matmul(X, [[0.8]]) + [[0.7]]  #moxing y=.8x+0.7 真实值
    #chushihua w权重 b偏置

    session = tf.compat.v1.keras.backend.get_session()
    weights = tf.Variable(initial_value=tf.compat.v1.random_normal([1, 1]),trainable=False, name='w')
    weights.eval(session)
    bias = tf.Variable(initial_value=tf.compat.v1.random_normal([1, 1]), name='b')
    bias.eval(session)

    y_predict = tf.matmul(X, weights) + bias #预测值

    #均方差算误差
    with tf.variable_creator_scope("error"):
        error = tf.reduce_mean(tf.square(y_predict - y_ture))

    tf.compat.v1.disable_eager_execution()
    tf.compat.v1.disable_v2_behavior()
    tf.compat.v1.get_default_graph()

    with tf.variable_creator_scope("optimizer"):
        optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=2).minimize(error)  #梯度下降
    #xuexibuchang

    #收集张量
    tf.summary.scalar('error', error)
    tf.summary.histogram('w', weights)
    tf.summary.histogram('b', bias)

    merge = tf.compat.v1.global_variables_initializer()
    # saver = tf.train.Saver()
    with tf.compat.v1.Session() as sess:
        sess.run(tf.compat.v1.global_variables_initializer())
        file_writer = tf.summary.SummaryWriter("./summary", graph=sess.graph)

        for i in range(100):
            sess.run(optimizer)
            print(sess.run(error))
            print(sess.run(weights))
            print(sess.run(bias))

            summary = sess.run(merge)
            file_writer.add_summary(summary, i)

            # saver.save(sess,"./checkpoint")
    return None

if __name__  ==  '__main__':
    linear_regress()