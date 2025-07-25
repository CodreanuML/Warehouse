#python imports

#django imports
from django.shortcuts import render,redirect,reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView,TemplateView
from django.views.generic.edit import FormView,CreateView,DeleteView,UpdateView
from django.http import HttpResponse
from django.core.paginator import Paginator


#app imports
from .models import Transport, TransportType, Route, LandTransport, NavalTransport, AirTransport
from .forms import TransportTypeForm,RouteForm,LandTransportForm,NavalTransportForm,AirTransportForm


#external imports


#main page for logistic app
class Main(View):
    def get(self, request):
        return render(request,'LogisticManager/main.html',None)




#Transport Type Subpages 
class Transport_Type_List_All(View):

    def get(self, request):
        transport_types = TransportType.objects.all()
        paginator = Paginator(transport_types, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "LogisticManager/transport_type_list.html", {
            "page_obj": page_obj
        })

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

class Routes_List_All(ListView):
    model = Route
    template_name = "LogisticManager/routes_list.html"
    paginate_by = 10  
      
    


class Routes_Create(FormView):
    template_name = 'LogisticManager/routes_create.html'
    form_class = RouteForm
    success_url = reverse_lazy('LogisticManager:successful')

    def form_valid(self, form):
        Route = form.save(commit=False)
        Route.save()
        return super().form_valid(form)    


class Routes_Update(UpdateView):
    model = Route   
    fields = ['route_type', 'from_T','to_T','length']
    template_name = 'LogisticManager/routes_update.html'
    success_url = reverse_lazy('LogisticManager:successful')


class Routes_Delete(DeleteView):
    model = Route
    template_name = 'LogisticManager/routes_delete.html'   
    success_url = reverse_lazy('LogisticManager:successful')



#General Pages
class Successful(TemplateView):
	template_name='general/successful.html'

class Failled(TemplateView):
	template_name='general/failled.html'