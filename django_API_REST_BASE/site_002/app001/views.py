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
from rest_framework import viewsets
from rest_framework.decorators import action

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class App001ViewSet(viewsets.ModelViewSet):
    queryset = App001.objects.all()
    serializer_class = App001Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly,)
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        app001 = self.get_object()
        return Response(app001.highlighted)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
"""
class App001Highlight(generics.GenericAPIView):
    queryset = App001.objects.all()
    renderer_class = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        app001 = self.get_object()
        return Response(app001.highlighted)
"""
@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        'users':reverse('user-list',request=request, format=format),
        'apps': reverse('app001-list', request=request, format=format)
    })
# Create your views here.
