# from django
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView,FormView,View,TemplateView,UpdateView,DetailView,ListView

# import from app
from scraps.forms import RegistrationForm,LoginForm,ScrapForm,UserProfileForm
from scraps.models import UserProfile,Scraps

# Create your views here.


class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm

    def get_success_url(self):
        return reverse("signin")

class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**Kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                return redirect("index")
        return render(request,"login.html",{"form":form})

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    
class IndexView(ListView):
    template_name="index.html"
    model=Scraps
    context_object_name="data"

class ProfileDetailView(DetailView):
    template_name="profile_detail.html"
    model=UserProfile
    context_object_name="data"

# localhost:8000/profile/<int:pk>/change

class ProfileUpdateView(UpdateView):
    template_name="profile_add.html"
    model=UserProfile
    form_class=UserProfileForm

    def get_success_url(self):
        return reverse("index")


class ScrapCreateView(CreateView):
    template_name="scrap_add.html"
    form_class=ScrapForm

    def get_success_url(self):
        return reverse("index")
    
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class ScrapDetailView(DetailView):
    template_name="scrap_detail.html"
    model=Scraps
    context_object_name="data"
