# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-18 13:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180218_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='imagae3',
            new_name='image3',
        ),
    ]