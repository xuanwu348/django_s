from app001.models import App001
from app001.serializers import App001Serializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from app001.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers


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

class App001Highlight(generics.GenericAPIView):
    queryset = App001.objects.all()
    renderer_class = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        app001 = self.get_object()
        return Response(app001.highlighted)

@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        'users':reverse('user-list',request=request, format=format),
        'apps': reverse('app001-list', request=request, format=format)
    })
# Create your views here.
