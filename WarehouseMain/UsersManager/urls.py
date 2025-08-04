from django.urls import include,path
from .views import RegisterView

app_name="UsersManager"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]