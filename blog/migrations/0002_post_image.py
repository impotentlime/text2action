# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-17 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='static/blog/images/text2action3.jpg', upload_to=''),
        ),
    ]
