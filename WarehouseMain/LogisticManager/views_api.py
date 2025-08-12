from rest_framework import viewsets
from .models import TransportType
from .serializers import TransportTypeSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator


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