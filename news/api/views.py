from rest_framework import generics
from .serializer import getAllNewsSerializer
from news.models import LatestNews


class getAllNews(generics.ListAPIView):

    serializer_class        = getAllNewsSerializer
    queryset                = LatestNews.objects.all()
