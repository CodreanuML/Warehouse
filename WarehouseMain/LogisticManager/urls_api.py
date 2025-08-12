from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import TransportTypeViewSet

router = DefaultRouter()
router.register(r'transport-types', TransportTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]