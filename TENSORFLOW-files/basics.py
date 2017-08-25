import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

n_class = 10
batch_size =100

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500
n_nodes_hl4 = 500
# sample images 'X'
x = tf.placeholder('float')
# sampl lables 'Y'
y = tf.placeholder('float')

def model(data):
    hiddenlayer1 = {'W':tf.Variable(tf.zeros([784, n_nodes_hl1])),
                    'B':tf.Variable(tf.zeros([n_nodes_hl1]))}

    hiddenlayer2 = {'W':tf.Variable(tf.zeros([n_nodes_hl1, n_nodes_hl2])),
                    'B':tf.Variable(tf.zeros([n_nodes_hl2]))}

    hiddenlayer3 = {"W":tf.Variable(tf.zeros([n_nodes_hl2, n_nodes_hl3])),
                    'B':tf.Variable(tf.zeros([n_nodes_hl3]))}

    hiddenlayer4 = {"W": tf.Variable(tf.zeros([n_nodes_hl3, n_nodes_hl4])),
                    'B': tf.Variable(tf.zeros([n_nodes_hl4]))}

    outputlayer = {"W":tf.Variable(tf.zeros([n_nodes_hl4, n_class])),
                    'B':tf.Variable(tf.zeros([n_class]))}

    l1 = tf.add(tf.matmul(data, hiddenlayer1['W']), hiddenlayer1['B'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hiddenlayer2['W']), hiddenlayer2['B'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hiddenlayer3['W']), hiddenlayer3['B'])
    l3 = tf.nn.relu(l3)

    l4 = tf.add(tf.matmul(l3, hiddenlayer4['W']), hiddenlayer4['B'])
    l4 = tf.nn.relu(l4)

    out = tf.add(tf.matmul(l4, outputlayer['W']), outputlayer['B'])

    return out

def train(idata):
    prediction = model(idata)

    i_hate_cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))

    my_optimiser = tf.train.AdamOptimizer(learning_rate=0.001).minimize(i_hate_cost)
    epochs = 10

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())


        for i in range(epochs):
            loss = 0
            for _ in range(int(mnist.train.num_examples/batch_size)):
                e_x, e_y = mnist.train.next_batch(batch_size)
                _, c = sess.run([my_optimiser, i_hate_cost], feed_dict={x:e_x, y:e_y})

                loss += c

            print("Epoch {} out of {} , loss: {}".format(i, epochs, loss))

        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

        print('Accuracy: {}'.format(accuracy.eval({x:mnist.test.images, y:mnist.test.labels})))

train(x)
