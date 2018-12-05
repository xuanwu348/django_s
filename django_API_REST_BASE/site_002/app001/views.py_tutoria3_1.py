#from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from app001.models import App001
from app001.serializers import App001Serializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class app001_list(APIView):
    def get(self, request, format=None):
        app1 = App001.objects.all()
        serializer = App001Serializer(app1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = App001Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREAT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class app001_detail(APIView):
    def get_object(self, pk):
        try:
            return App001.objects.all()
        except App001.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        app1 = self.get_object(pk)
        serializer = App001Serializer(app1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        app1 = self.get_object(pk)
        app1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# Create your views here.
