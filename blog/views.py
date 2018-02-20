from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from .models import Post
import random
import tensorflow as tf
import matplotlib.pyplot as plt
from .forms import PostForm

"""
TUTORIAL CODES
############################################################
post_<something> htmls and view functions are from tutorials
############################################################
"""

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

"""
PROJECT CODES
############################################################
final_<something> htmls and view functions are changed
version of tutorial codes for the project
############################################################
"""


def final_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/final_list.html', {'posts': posts})

def final_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/final_detail.html', {'post': post})

def final_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('final_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/final_edit.html', {'form': form})

"""
TEST CODES
############################################################
Written for try new things out, such as applying basic
tensorflow and matplotlib codes.
############################################################
"""

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

"""
def test(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/test.html', {'post': post})
"""
