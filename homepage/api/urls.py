from .views import allHomepageSliderImages, allTestimonialView
from django.urls import path, include

urlpatterns = [
      # path('create', createClient.as_view(), name="createClient"),
      path('homepageslider', allHomepageSliderImages.as_view(), name="homepageslider"),
      path('testimonial', allTestimonialView.as_view(), name="homepageslider"),
      ]
