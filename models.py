# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Bag(models.Model):
  id = models.AutoField(primary_key=True)

class User(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(unique=True, max_length=30)
  bag = models.ForeignKey(Bag)

class FcmToken(models.Model):
  id = models.AutoField(primary_key=True)
  body = models.CharField(max_length=200)
  user = models.ForeignKey(User)
  
  
  
