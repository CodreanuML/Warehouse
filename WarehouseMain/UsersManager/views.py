from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import ProfileCreationForm


class RegisterView(CreateView):
    model = User
    form_class = ProfileCreationForm
    template_name = 'UsersManager/register.html'  
    success_url = reverse_lazy('LogisticManager:successful')