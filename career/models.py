from django.db import models
from django.conf import settings

# Create your models here.
class job_category(models.Model):
    class Meta:
        verbose_name_plural = "Job Category"


    name               = models.CharField(max_length=100, null=True, blank=True)

    
    #timestamps
    created_date       = models.DateTimeField(auto_now_add=True)
    modified_date      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
        
class job_opening(models.Model):
    class Meta:
        verbose_name_plural = "Job Openings"


    category            = models.ForeignKey(job_category, null=False, on_delete=models.CASCADE)
    title               = models.CharField( max_length=100, null=True, blank=True)
    location            = models.CharField(  max_length=100, blank=True)
    job_type            = models.CharField( max_length=100, blank=True, help_text="Full Time / Part Time")

    
    #timestamps
    created_date       = models.DateTimeField(auto_now_add=True)
    modified_date      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
