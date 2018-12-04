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

"""
@csrf_exempt
def app001_list(request):
    if request.method == "GET":
        app1 = App001.objects.all()
        serializer = App001Serializer(app1, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = App001Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResonse(serializer.data, status=201)
        return JsonResonse(serializer.errors, status=400)
"""

@api_view(["GET","POST"])
def app001_list(request, format=None):
    if request.method == "GET":
        app1 = App001.objects.all()
        serilizer = App001Serializer(app1, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = App001Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
@csrf_exempt
def app001_detail(request, pk):
    try:
        app1 = App001.objects.get(pk=pk)
    except App001.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = App001Serializer(app1)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = App001Serializer(app1, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResonse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        app1.delete()
        return HttpResponse(status=204)
"""

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
