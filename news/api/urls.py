from .views import getAllNews, getAllBlog
from django.urls import path, include

urlpatterns = [
      path('getAllNews', getAllNews.as_view(), name="getAllNews"),
      path('getAllBlog', getAllBlog.as_view(), name="getAllBlog"),
      ]
