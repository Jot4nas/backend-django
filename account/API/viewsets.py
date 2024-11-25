from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from account.API import serializers
from account import models
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend


class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegisterSerializers
    queryset = models.Register.objects.all()

