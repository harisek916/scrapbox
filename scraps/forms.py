# from django
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# from app
from scraps.models import Scraps,UserProfile,Categories
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
        widgets={
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
            "profile_pic":forms.FileInput(attrs={"class":"form-control"})

        }


class ScrapForm(forms.ModelForm):
    class Meta:
        model=Scraps
        exclude=('user','status')
        widgets={
                "category":forms.Select(attrs={"class":"form-control"}),
                "name":forms.TextInput(attrs={"class":"form-control"}),
                "condition":forms.TextInput(attrs={"class":"form-control"}),
                "price":forms.NumberInput(attrs={"class":"form-control"}),
                "price":forms.NumberInput(attrs={"class":"form-control"}),
                "picture":forms.FileInput(attrs={"class":"form-control"}),
                "place":forms.TextInput(attrs={"class":"form-control"})
        }
