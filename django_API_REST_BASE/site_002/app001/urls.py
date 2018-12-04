from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app001 import views

urlpatterns = [
    path("apps/", views.app001_list),
    path('apps/<int:pk>', views.app001_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
