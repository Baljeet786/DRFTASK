from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CustomUserProfileForm(UserCreationForm):
    class Meta:
        fields = '__all__'
