from django.urls import path
from app001 import views

urlpatterns = [
    path("apps/", views.app001_list),
    path('apps/<int:pk>/', views.app001_detail),
]
