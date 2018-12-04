#from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from app001.models import App001
from app001.serializers import App001Serializer


@api_view(["GET","POST"])
def app001_list(request, format=None):
    if request.method == "GET":
        app1 = App001.objects.all()
        serializer = App001Serializer(app1, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = App001Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])
def app001_detail(request, pk, format=None):
    try:
        app1 = App001.objects.get(pk=pk)
    except App001.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = App001Serializer(app1)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = App001Serializer(app1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        app1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# Create your views here.
