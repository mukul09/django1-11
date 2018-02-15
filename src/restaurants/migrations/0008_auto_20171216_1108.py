# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-16 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20171216_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurantlocation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
