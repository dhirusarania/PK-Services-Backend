from rest_framework import serializers
from clientlist.models import ClientListKamrup, ClientListOutside


class ClientListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ClientListKamrup
        fields = "__all__"
