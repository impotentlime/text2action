from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django import forms
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    summary = models.TextField(default='')
    content = models.TextField(default='')
    references = models.TextField(default='')
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
