from app001.models import App001
from app001.serializers import App001Serializer
from rest_framework import generics

class app001_list(generics.ListCreateAPIView):
    queryset = App001.objects.all()
    serializer_class = App001Serializer
    

class app001_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = App001.objects.all()
    serializer_class = App001Serializer
    
# Create your views here.
