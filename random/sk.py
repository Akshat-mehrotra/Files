import tensorflow as tf
import numpy as np

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

images = tf.placeholder(tf.float32, [None, 784])

W = tf.Variable