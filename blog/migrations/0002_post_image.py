# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-06-10 08:14
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
            field=models.ImageField(default='', upload_to='intruder_image/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
