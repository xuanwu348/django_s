from django.urls import path, include
from app001 import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title="Pastebin API")
router = DefaultRouter()
router.register(r'app001s', views.App001ViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [path("", include(router.urls)),
               path("schema/", schema_view),
              ]
#urlpatterns = format_suffix_patterns(urlpatterns)
