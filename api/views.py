from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets

from api.serializers import ScrapSerializer
from scraps.models import Scraps


# Create your views here.

class ScrapModelViewSetView(viewsets.ModelViewSet):
    serializer_class=ScrapSerializer
    model=Scraps
    queryset=Scraps.objects.all()