from rest_framework import serializers
from homepage.models import HomepageSlider, Testimonial


class HomepageImagesSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = HomepageSlider
        fields = "__all__"

class allTestimonialViewSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Testimonial
        fields = "__all__"
