from django.urls import include,path
from .views import RegisterView,Login,PreLogOut , MyPasswordResetView , MyPasswordResetDoneView , MyPasswordResetConfirmView , MyPasswordResetCompleteView
from django.contrib.auth.views import LogoutView 
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name="UsersManager"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/',Login.as_view(),name='login'),
    path('prelogout/',PreLogOut.as_view(),name='prelogout'),
    path('logout/',LogoutView.as_view(),name='logout'),

    #password reset flow
    path('password-reset/', MyPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]