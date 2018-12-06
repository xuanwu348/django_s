from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app001 import views

urlpatterns = [
    path("apps/", views.app001_list.as_view(), name="app001-list"),
    path('apps/<int:pk>', views.app001_detail.as_view(),name="app001-detail"),
    path('users/', views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(),name='user-detail'),
    path('app001s/<int:pk>/highlight/',views.App001Highlight.as_view(),name="app001-highlight"),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
