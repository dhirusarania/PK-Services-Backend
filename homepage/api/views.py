from rest_framework import generics
from homepage.models import HomepageSlider, Testimonial
from .serializer import HomepageImagesSerializer, allTestimonialViewSerializer

class allHomepageSliderImages(generics.ListAPIView):

    serializer_class        = HomepageImagesSerializer
    queryset                = HomepageSlider.objects.all()


class allTestimonialView(generics.ListAPIView):

    serializer_class        = allTestimonialViewSerializer
    queryset                = Testimonial.objects.all()





