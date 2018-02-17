from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Post
import random
import tensorflow as tf
import matplotlib.pyplot as plt

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def helloworld(request, num1, num2):
    # logs_path = ''
    n1 = int(num1)
    n2 = int(num2)

    x = tf.placeholder(tf.int32)
    y = tf.placeholder(tf.int32)

    add = tf.add(x,y)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        z = sess.run(add, feed_dict = {x:n1, y:n2})

    return HttpResponse("sum of %s and %s is %s" % (num1, num2, z))
# Create your views here.

def plot(request):
    X = [1,2,3]
    Y = [1,2,3]
    W = tf.placeholder(tf.float32)
    hypothesis = X * W

    cost = tf.reduce_mean(tf.square(hypothesis - Y))
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    W_val = []
    cost_val = []

    for i in range(-30, 50):
        feed_W = i * 0.1
        curr_cost, curr_W = sess.run([cost, W], feed_dict = {W: feed_W})
        W_val.append(curr_W)
        cost_val.append(curr_cost)

    plt.plot(W_val, cost_val)
    plt.show()

    return HttpResponse("%s %s" % (W_val, cost_val))
