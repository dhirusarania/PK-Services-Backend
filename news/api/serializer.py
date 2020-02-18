from rest_framework import serializers
from news.models import LatestNews, BlogPost

class getAllNewsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = LatestNews
        fields = "__all__"

class getAllBlogSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = BlogPost
        fields = "__all__"