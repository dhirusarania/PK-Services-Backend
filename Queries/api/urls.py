from .views import createQuery, createContact, sendMail
from django.urls import path, include

urlpatterns = [
      path('createQuery', createQuery.as_view(), name="createQuery"),
      path('createContact', createContact.as_view(), name="createContact"),
      path('sendmail', sendMail.as_view(), name="sendMail"),
      ]
