from .views import allHomepageSliderImages
from django.urls import path, include

urlpatterns = [
      # path('create', createClient.as_view(), name="createClient"),
      path('homepageslider', allHomepageSliderImages.as_view(), name="homepageslider"),
      ]
