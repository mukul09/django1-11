# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-16 11:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20171216_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantlocation',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='restaurantlocation',
            name='updated',
        ),
    ]