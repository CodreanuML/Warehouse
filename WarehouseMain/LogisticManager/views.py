#python imports

#django imports
from django.shortcuts import render,redirect,reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView,CreateView,DeleteView,UpdateView
from django.http import HttpResponse


#app imports
from .models import Transport, TransportType, Route, LandTransport, NavalTransport, AirTransport
from .forms import TransportTypeForm,RouteForm,LandTransportForm,NavalTransportForm,AirTransportForm


#external imports


#main page for logistic app
class Main(View):
    def get(self, request):
        return render(request,'LogisticManager/main.html',None)




#Transport Type Subpages 
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

#Routes Subpages
class Routes_Create(FormView):
    template_name = 'LogisticManager/routes_create.html'
    form_class = RouteForm
    success_url = reverse_lazy('LogisticManager:successful')

    def form_valid(self, form):
        Route = form.save(commit=False)
        Route.save()
        return super().form_valid(form)    


class Routes_Update(View):
    pass


class Routes_Delete(DeleteView):
    pass



#General Pages
class Successful(TemplateView):
	template_name='general/successful.html'

class Failled(TemplateView):
	template_name='general/failled.html'