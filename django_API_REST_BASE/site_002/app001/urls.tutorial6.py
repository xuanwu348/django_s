from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app001.views import App001ViewSet, UserViewSet, api_root
from rest_framework import renderers

app001_list = App001ViewSet.as_view({
                'get': 'list',
                'post': 'create'
              })
app001_detail = App001ViewSet.as_view({
                'get':"retrieve",
                'put':"update",
                'patch':'partial_update',
                'delete':'destroy'
              })
app001_highlight = App001ViewSet.as_view({
                'get':"highlight"
              },renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
                 "get":"list"
               })
user_detail = UserViewSet.as_view({
                 "get":"retrieve"
               })

urlpatterns = [
    path("apps/", app001_list, name="app001-list"),
    path('apps/<int:pk>', app001_detail, name="app001-detail"),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('app001s/<int:pk>/highlight/',app001_highlight, name="app001-highlight"),
    path("", api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
