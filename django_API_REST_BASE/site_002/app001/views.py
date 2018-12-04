from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from app001.models import App001
from app001.serializers import App001Serializer

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





# Create your views here.
