# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-06-10 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='intruder_image/default_error.png', upload_to='intruder_image/%Y/%m/%d/'),
        ),
    ]
