# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_auto_20170423_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
