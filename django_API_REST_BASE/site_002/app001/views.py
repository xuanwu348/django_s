from app001.models import App001
from app001.serializers import App001Serializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from app001.permissions import IsOwnerOrReadOnly


class app001_list(generics.ListCreateAPIView):
    queryset = App001.objects.all()
    serializer_class = App001Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class app001_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = App001.objects.all()
    serializer_class = App001Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    querySet = User.objects.all()
    serializer_class = UserSerializer
# Create your views here.
