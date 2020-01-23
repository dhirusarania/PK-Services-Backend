from rest_framework import serializers
from whatwedo.models import pksercurity, pkservices


class pksercuritySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = pksercurity
        fields = "__all__"

class pkservicesSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = pkservices
        fields = "__all__"
