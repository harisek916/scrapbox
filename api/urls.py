from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

router=DefaultRouter()
router.register("scraps",views.ScrapModelViewSetView,basename="scraps")



urlpatterns=[

]+router.urls