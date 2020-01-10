from .views import getAllNews
from django.urls import path, include

urlpatterns = [
      path('getAllNews', getAllNews.as_view(), name="getAllNews"),
      ]
