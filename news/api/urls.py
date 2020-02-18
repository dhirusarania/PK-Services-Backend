from .views import getAllNews, getAllBlog, getSingleBlog
from django.urls import path, include

urlpatterns = [
      path('getAllNews', getAllNews.as_view(), name="getAllNews"),
      path('getAllBlog', getAllBlog.as_view(), name="getAllBlog"),
      path('getSingleBlog/<int:pk>', getSingleBlog.as_view(), name="getSingleBlog"),
      ]
