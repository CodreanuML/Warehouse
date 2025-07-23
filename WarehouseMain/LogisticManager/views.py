from django.shortcuts import render,redirect,reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.http import HttpResponse

from .models import Transport, TransportType, Route, LandTransport, NavalTransport, AirTransport


class Main(View):
    def get(self, request):
        return render(request,'LogisticManager/main.html',None)


class Transport_Type_Create(CreateView):
    model = TransportType	
    fields = ['name', 'category','capacity','capacity_unit']
    template_name = 'LogisticManager/transport_type_create.html'
    success_url = reverse_lazy('LogisticManager:successful')
    def get_initial(self,*args,**kwargs):
    	initial=super().get_initial(**kwargs)
    	initial['name']="Introduceti numele Transportului"
    	return initial

class Transport_Type_Update(UpdateView):
    model = TransportType	
    fields = ['name', 'category','capacity','capacity_unit']
    template_name = 'LogisticManager/transport_type_update.html'
    success_url = reverse_lazy('LogisticManager:successful')

class Transport_Type_Delete(DeleteView):
    model = TransportType
    template_name = 'LogisticManager/transport_type_delete.html'	
    success_url = reverse_lazy('LogisticManager:successful')


class Successful(TemplateView):
	template_name='general/successful.html'

class Failled(TemplateView):
	template_name='general/failled.html'