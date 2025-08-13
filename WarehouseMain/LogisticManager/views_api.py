from rest_framework import viewsets
from .models import TransportType,Route
from .serializers import TransportTypeSerializer , RoutesTypeSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect,reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view



@method_decorator(csrf_exempt, name='dispatch')
class TransportTypeViewSet(viewsets.ModelViewSet):

    queryset = TransportType.objects.all() 

    serializer_class = TransportTypeSerializer

    def get_queryset(self):

        queryset = super().get_queryset()  

        pk_id = self.request.query_params.get('pk')
        if pk_id:
            queryset = queryset.filter(pk=pk_id)
        return queryset


@api_view(['GET'])
def RoutesViewSet(request):
    queryset = Route.objects.all()
    serializer = RoutesTypeSerializer(queryset, many=True)
    return Response(serializer.data)