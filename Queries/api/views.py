from rest_framework import generics
from .serializer import createQuerySerializer, createContactSerializer
from Queries.models import CareerQuery, ContactUs


class createQuery(generics.CreateAPIView):

    serializer_class        = createQuerySerializer
    queryset                = CareerQuery.objects.all()

class createContact(generics.CreateAPIView):

    serializer_class        = createContactSerializer
    queryset                = ContactUs.objects.all()