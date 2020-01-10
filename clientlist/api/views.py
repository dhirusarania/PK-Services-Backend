from rest_framework import generics
from .serializer import ClientListSerializer
from clientlist.models import ClientListKamrup , ClientListOutside


class allKamrup(generics.ListAPIView):

    serializer_class        = ClientListSerializer
    queryset                = ClientListKamrup.objects.all()

class allOutside(generics.ListAPIView):

    serializer_class        = ClientListSerializer
    queryset                = ClientListOutside.objects.all()



    





