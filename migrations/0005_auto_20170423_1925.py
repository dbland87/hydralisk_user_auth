# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_auto_20170423_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]