# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 17:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fcmtoken',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='bag_id',
            new_name='bag',
        ),
    ]
