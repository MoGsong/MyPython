import tensorflow as tf

tf.compat.v1.disable_eager_execution()

mat0 = tf.constant([[0,0,0],[0,0,0]])
mat1 = tf.zeros([2])
mat2 = tf.ones([3,3])
mat3 = tf.fill([2,3],15)
mat4 = tf.zeros_like(mat3)
mat5 = tf.linspace(0.0,2.0,10)
mat6 = tf.random.uniform([2,3])
with tf.compat.v1.Session() as sess:
    print(sess.run(mat0))
    print(sess.run(mat1))
    print(sess.run(mat2))
    print(sess.run(mat3))
    print(sess.run(mat4))
    print(sess.run(mat5))
    print(sess.run(mat6))
