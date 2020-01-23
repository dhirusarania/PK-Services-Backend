from .views import career
from django.urls import path, include

urlpatterns = [
      # path('create', createClient.as_view(), name="createClient"),
      path('', career.as_view()),
      ]
