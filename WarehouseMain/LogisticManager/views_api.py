from rest_framework import viewsets
from .models import TransportType,Route
from .serializers import TransportTypeSerializer , RoutesTypeSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect,reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse



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
    if request.method=="GET":
        queryset = Route.objects.all()
        serializer = RoutesTypeSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def RouteDetailView(request,pk):
    
    try:
        queryset=Route.objects.get(pk=pk)
    except Route.DoesNotExist:
        return HttpResponse(status=404)


    if request.method=="GET":
        serializer=RoutesTypeSerializer(queryset)
        return Response(serializer.data)

