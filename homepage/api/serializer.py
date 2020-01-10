from rest_framework import serializers
from homepage.models import HomepageSlider


class HomepageImagesSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = HomepageSlider
        fields = "__all__"
