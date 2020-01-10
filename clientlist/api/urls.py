from .views import allKamrup, allOutside
from django.urls import path, include

urlpatterns = [
      path('allKamrup', allKamrup.as_view(), name="allClient"),
      path('allOutside', allOutside.as_view(), name="allClient"),
      ]
