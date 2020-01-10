from rest_framework import serializers
from Queries.models import CareerQuery, ContactUs


class createQuerySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CareerQuery
        fields = "__all__"

class createContactSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ContactUs
        fields = "__all__"
