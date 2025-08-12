from django.urls import include, path
from . import views as LogisticViews


app_name = "LogisticManager"


urlpatterns = [ 
				#main
					
				path('main/',LogisticViews.Main.as_view(),name='main'),
				
				path('main/data/', LogisticViews.MainDataView.as_view(), name='main-data'),

				#transport_type
				
				path('transport_type/',LogisticViews.Transport_Type_List_All.as_view(),name='transport_type_list_all'),

				path('transport_type/create/',LogisticViews.Transport_Type_Create.as_view(),name='transport_type_create'),

				path('transport_type/update/<int:pk>/',LogisticViews.Transport_Type_Update.as_view(),name='transport_type_update'),

				path('transport_type/delete/<int:pk>/',LogisticViews.Transport_Type_Delete.as_view(),name='transport_type_delete'),

				#routes

				path('routes/',LogisticViews.Routes_List_All.as_view(),name='routes_list_all'),

				path('routes/create/',LogisticViews.Routes_Create.as_view(),name='routes_create'),

				path('routes/update/<int:pk>/',LogisticViews.Routes_Update.as_view(),name='routes_update'),

				path('routes/delete/<int:pk>/',LogisticViews.Routes_Delete.as_view(),name='routes_delete'),

				#land transport

				path('landtransport/',LogisticViews.LandTransport_List_All.as_view(),name='land_transport_all'),

				path('landtransport/create/',LogisticViews.LandTransport_Create.as_view(),name='land_transport_create'),

				path('landtransport/update/<int:pk>/',LogisticViews.LandTransport_Update.as_view(),name='land_transport_update'),

				path('landtransport/delete/<int:pk>/',LogisticViews.LandTransport_Delete.as_view(),name='land_transport_delete'),

				#naval transport

				path('airtransport/',LogisticViews.AirTransport_List_All.as_view(),name='air_transport_all'),

				path('airtransport/create/',LogisticViews.AirTransport_Create.as_view(),name='air_transport_create'),

				path('airtransport/update/<int:pk>/',LogisticViews.AirTransport_Update.as_view(),name='air_transport_update'),

				path('airtransport/delete/<int:pk>/',LogisticViews.AirTransport_Delete.as_view(),name='air_transport_delete'),

				#air transport

				path('navaltransport/',LogisticViews.NavalTransport_List_All.as_view(),name='naval_transport_all'),

				path('navaltransport/create/',LogisticViews.NavalTransport_Create.as_view(),name='naval_transport_create'),

				path('navaltransport/update/<int:pk>/',LogisticViews.NavalTransport_Update.as_view(),name='naval_transport_update'),

				path('navaltransport/delete/<int:pk>/',LogisticViews.NavalTransport_Delete.as_view(),name='naval_transport_delete'),

				#general

				path('successful/',LogisticViews.Successful.as_view(),name='successful'),

				path('failled/',LogisticViews.Failled.as_view(),name='failled'),



]