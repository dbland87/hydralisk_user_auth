from user_auth.models import User, Bag, FcmToken

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'name', 'bag')


class BagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bag
    fields = ('id')

class FcmTokenSerializer(serializers.ModelSerializer):
  class Meta:
    model = FcmToken
    fields = ('id', 'body', 'user')

