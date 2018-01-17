from django import forms
from salon.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Please enter a username")
	password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter your password")
	email = forms.CharField(help_text="Please enter your email", required=False)

	class Meta:
		model = User
		fields = ['username', 'password', 'email']

class UserProfileForm(forms.ModelForm):
	picture = forms.ImageField(help_text="Choose a profile picture", required=False)

	class Meta:
		model = UserProfile
		fields = ['picture']