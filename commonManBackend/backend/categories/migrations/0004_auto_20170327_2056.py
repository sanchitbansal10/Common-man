# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20170327_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryitem',
            name='category',
        ),
        migrations.AddField(
            model_name='categoryitem',
            name='category',
            field=models.ManyToManyField(to='categories.Menu'),
        ),
    ]
