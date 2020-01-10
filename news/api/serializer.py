from rest_framework import serializers
from news.models import LatestNews

class getAllNewsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = LatestNews
        fields = "__all__"