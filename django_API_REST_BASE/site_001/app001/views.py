from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from app001.serializers import UserSerializer, GroupSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset =  User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
