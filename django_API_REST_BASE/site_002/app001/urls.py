from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app001 import views

urlpatterns = [
    path("apps/", views.app001_list.as_view()),
    path('apps/<int:pk>', views.app001_detail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
