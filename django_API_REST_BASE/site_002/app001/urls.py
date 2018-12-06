from django.urls import path, include
from app001 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'app001s', views.App001ViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [path("", include(router.urls)),]
#urlpatterns = format_suffix_patterns(urlpatterns)
