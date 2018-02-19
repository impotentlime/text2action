from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django import forms
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    text = models.TextField()
    test = HTMLField(default='')
    content = models.TextField(default='content')
    image = models.ImageField(default = 'static/blog/images/text2action3.jpg')
    image2 = models.ImageField(default = 'static/blog/images/blank.jpg')
    image3 = models.ImageField(default = 'static/blog/images/blank.jpg')
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
