# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-19 06:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-updated', '-timestamp']},
        ),
    ]
