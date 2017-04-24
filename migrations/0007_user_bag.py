# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0006_remove_user_bag'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bag',
            #field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='user_auth.Bag'),
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_auth.Bag'),
            preserve_default=False,
        ),
    ]