from rest_framework import generics
from career.models import job_opening
from .serializer import job_openingSerializer
from django.db.models import F
from rest_framework.response import Response
from rest_framework import status

class career(generics.ListAPIView):

    serializer_class        = job_openingSerializer
    queryset                = job_opening.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        department = job_opening.objects.all().values(
            'id',
            'title',
            'location',
            'job_type',
            'experience',
            'open_positions',
            'salary_range',
            category_name=F('category__name'),
        )
        return Response(list(department), status=status.HTTP_200_OK)

