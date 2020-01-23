from rest_framework import serializers
from career.models import job_opening


class job_openingSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = job_opening
        fields = "__all__"