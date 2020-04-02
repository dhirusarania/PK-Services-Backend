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
    title               = models.CharField( max_length=100, null=True, blank=True, help_text="Optional")
    location            = models.CharField(  max_length=100, blank=True)
    job_type            = models.CharField( max_length=100, blank=True, help_text="Full Time / Part Time")
    experience          = models.CharField( max_length=100, blank=True, help_text="Experience")
    salary_range        = models.CharField( max_length=100, blank=True, help_text="1.5 - 2.5 Lac")
    open_positions      = models.CharField( max_length=100, blank=True, help_text="Number of Empty Positions")

    
    #timestamps
    created_date       = models.DateTimeField(auto_now_add=True)
    modified_date      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
