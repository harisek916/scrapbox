from django.urls import path
from scraps import views


urlpatterns=[
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("login/",views.SignInView.as_view(),name="signin"),
    path("logout/",views.SignOutView.as_view(),name="signout"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("profile/<int:pk>/change/",views.ProfileUpdateView.as_view(),name="profile-update"),
    path("scrap/add",views.ScrapCreateView.as_view(),name="scrap-create"),
    path("profile/<int:pk>/",views.ProfileDetailView.as_view(),name="profile-detail"),
    path("scraps/<int:pk>/",views.ScrapDetailView.as_view(),name="scrap-detail"),
    path("scraps/<int:pk>/change/",views.ScrapUpdateView.as_view(),name="scrap-update"),
    path("scraps/<int:pk>/remove/",views.ScrapDeleteView.as_view(),name="scrap-delete"),
]