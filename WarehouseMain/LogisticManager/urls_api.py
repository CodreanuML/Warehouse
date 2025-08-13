from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import TransportTypeViewSet , RoutesViewSet ,RouteDetailView

router = DefaultRouter()
router.register(r'transport-types', TransportTypeViewSet)

urlpatterns = [

    path('', include(router.urls)),

    path('routes/',RoutesViewSet,name="routes"),

    path('routes/<pk>/',RouteDetailView,name="route")
]