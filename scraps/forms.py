# from django
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# from app
from scraps.models import Scraps,UserProfile
# forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2",]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=('user',)

class ScrapForm(forms.ModelForm):
    class Meta:
        model=Scraps
        exclude=('user','status')
