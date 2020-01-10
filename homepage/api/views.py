from rest_framework import generics
from homepage.models import HomepageSlider
from .serializer import HomepageImagesSerializer

class allHomepageSliderImages(generics.ListAPIView):

    serializer_class        = HomepageImagesSerializer
    queryset                = HomepageSlider.objects.all()





