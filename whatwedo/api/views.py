from rest_framework import generics
from whatwedo.models import pkservices, pksercurity
from .serializer import pkservicesSerializer, pksercuritySerializer

class security(generics.ListAPIView):

    serializer_class        = pksercuritySerializer
    queryset                = pksercurity.objects.all()


class services(generics.ListAPIView):

    serializer_class        = pkservicesSerializer
    queryset                = pkservices.objects.all()





