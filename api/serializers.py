from rest_framework import serializers
from scraps.models import Scraps



class ScrapSerializer(serializers.ModelSerializer):

    class Meta:
        model=Scraps
        fields="__all__"
        read_only_fields=["id","status","picture"]