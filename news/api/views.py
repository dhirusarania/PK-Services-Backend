from rest_framework import generics
from .serializer import getAllNewsSerializer, getAllBlogSerializer
from news.models import LatestNews, BlogPost


class getAllNews(generics.ListAPIView):

    serializer_class        = getAllNewsSerializer
    queryset                = LatestNews.objects.all()

class getAllBlog(generics.ListAPIView):

    serializer_class        = getAllBlogSerializer
    queryset                = BlogPost.objects.all().order_by('-pk')

class getSingleBlog(generics.RetrieveAPIView):

    lookup_field            = 'pk'
    serializer_class        = getAllBlogSerializer
    queryset                = BlogPost.objects.all()
