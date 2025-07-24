from django.urls import include, path

app_name = "LogisticManager"

from . import views as LogisticViews

urlpatterns = [ 
				#main
					
				path('main/',LogisticViews.Main.as_view(),name='main'),

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


				#general

				path('successful/',LogisticViews.Successful.as_view(),name='successful'),

				path('failled/',LogisticViews.Failled.as_view(),name='failled'),
]