# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-18 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
