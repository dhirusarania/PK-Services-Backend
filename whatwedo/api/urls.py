from .views import security, services
from django.urls import path, include

urlpatterns = [
      # path('create', createClient.as_view(), name="createClient"),
      path('security', security.as_view(), name="homepageslider"),
      path('services', services.as_view(), name="asas"),
      ]
