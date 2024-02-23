"""
URL configuration for scrapbox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from scraps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register",views.SignUpView.as_view(),name="signup"),
    path("login",views.SignInView.as_view(),name="signin"),
    path("logout",views.SignOutView.as_view(),name="signout"),
    path("index",views.IndexView.as_view(),name="index"),
    path("profile/<int:pk>/change",views.ProfileUpdateView.as_view(),name="profile-update"),
    path("scrap/add",views.ScrapCreateView.as_view(),name="scrap-create"),
    path("profile/<int:pk>",views.ProfileDetailView.as_view(),name="profile-detail"),
    path("scraps/<int:pk>",views.ScrapDetailView.as_view(),name="scrap-detail"),
    path("scraps/<int:pk>/change",views.ScrapUpdateView.as_view(),name="scrap-update"),
    path("scraps/<int:pk>/remove",views.ScrapDeleteView.as_view(),name="scrap-delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
