from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileCreationForm(UserCreationForm):
	email=forms.EmailField(required=True)
	role=forms.ChoiceField(choices=Profile.ROLE_CHOICE)
	id_number=forms.IntegerField(required=True)
	first_name = forms.CharField(max_length=30, required=True)
	last_name = forms.CharField(max_length=30, required=True)

	class Meta:
		model=User
		fields=('username','email','first_name','last_name','password1','password2','role','id_number')

	def save(self,commit=True):
		user=super().save(commit=False)
		user.email=self.cleaned_data['email']
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		if commit:
			user.save()

			Profile.objects.create(
				user=user,	
				role=self.cleaned_data['role'],
				id_number=self.cleaned_data['id_number']

			)

		return user