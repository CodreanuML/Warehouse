from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import ProfileCreationForm
from django.views.generic import ListView,TemplateView


#views for handling user operation 

class RegisterView(CreateView):
    model = User
    form_class = ProfileCreationForm
    template_name = 'UsersManager/register.html'  
    success_url = reverse_lazy('LogisticManager:successful')


class Login(LoginView):
    template_name = "UsersManager/login.html"
    success_url = reverse_lazy('LogisticManager:successful')


class PreLogOut(TemplateView):
    template_name="UsersManager/logout.html"


class MyPasswordResetView(auth_views.PasswordResetView):
    template_name = 'UsersManager/password_reset.html'
    email_template_name = 'UsersManager/password_reset_email.html'
    subject_template_name = 'UsersManager/password_reset_subject.txt'
    success_url = reverse_lazy('UsersManager:password_reset_done')


class MyPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'UsersManager/password_reset_done.html'


class MyPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'UsersManager/password_reset_confirm.html'
    success_url = reverse_lazy('UsersManager:password_reset_complete')


class MyPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'UsersManager/password_reset_complete.html'


