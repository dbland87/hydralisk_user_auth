# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.utils.six import BytesIO

from user_auth.models import *
from user_auth.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser


# Create your views here.

class RequestUser(APIView):

  def post(self, request, format=None):
    #Check if user exists
    data = JSONParser().parse(request)
    name = data['user']['name']
    if User.objects.filter(name = name).exists():
      user = User.objects.get(name = name)
      serializer = UserSerializer(user)
      return Response({"user" : serializer.data}, status=250)
    else:
      #User does not exist. Create a new user and bag 
      bag = Bag.objects.create()
      bag.save()
      data['bag'] = bag.id
      serializer = UserSerializer(data=data)

      if serializer.is_valid():
        serializer.save()
        return Response({"user" : serializer.data}, status=status.HTTP_201_CREATED)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

  

