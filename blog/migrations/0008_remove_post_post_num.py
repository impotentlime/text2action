# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-18 16:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_num',
        ),
    ]
