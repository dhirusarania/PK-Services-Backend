from .views import createQuery, createContact
from django.urls import path, include

urlpatterns = [
      path('createQuery', createQuery.as_view(), name="createQuery"),
      path('createContact', createContact.as_view(), name="createContact"),
      ]
