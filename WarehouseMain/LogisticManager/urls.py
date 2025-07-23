from django.urls import include, path

app_name = "LogisticManager"

from . import views as LogisticViews

urlpatterns = [ 
				path('main/',LogisticViews.Main.as_view(),name='main'),

				path('transport_type/create/',LogisticViews.Transport_Type_Create.as_view(),name='transport_type_create'),

				path('transport_type/update/<int:pk>/',LogisticViews.Transport_Type_Update.as_view(),name='transport_type_update'),

				path('transport_type/delete/<int:pk>/',LogisticViews.Transport_Type_Delete.as_view(),name='transport_type_delete'),

				path('successful/',LogisticViews.Successful.as_view(),name='successful'),

				path('failled/',LogisticViews.Failled.as_view(),name='failled'),
]