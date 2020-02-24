from abc import ABC
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from myshots.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyScreen
        fields = ['img']
