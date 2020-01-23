from django.db import models
from django.conf import settings

# Create your models here.
class pksercurity(models.Model):
    class Meta:
        verbose_name_plural = "PK Security Services"


    title               = models.CharField(max_length=100, null=True, blank=True)
    content             = models.TextField( null=True, blank=True)

    
    #timestamps
    created_date       = models.DateTimeField(auto_now_add=True)
    modified_date      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

# Create your models here.
class pkservices(models.Model):
    class Meta:
        verbose_name_plural = "PK Services"


    title               = models.CharField(max_length=100, null=True, blank=True)
    content             = models.TextField( null=True, blank=True)

    
    #timestamps
    created_date       = models.DateTimeField(auto_now_add=True)
    modified_date      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)