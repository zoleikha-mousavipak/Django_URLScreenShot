from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *
from myshots.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ShotViewSet(viewsets.ModelViewSet):
    queryset = MyScreen.objects.all()
    serializer_class = ShotSerializer(queryset, many=True)

    # @api_view(['GET', 'POST'])
    # def api_shots(self, format=None):
    #
    #     return Response("test")
    #     # return Response(serializer_class.data)






