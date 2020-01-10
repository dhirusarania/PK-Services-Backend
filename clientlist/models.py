from django.db import models

# Create your models here.
class ClientListKamrup(models.Model):
    class Meta:
        verbose_name_plural = "Client List Locations in Kamrup"


    name               = models.CharField(max_length=100, null=True, blank=True)
    location_name      = models.CharField(max_length=100, null=True, blank=True)
    latitude           = models.DecimalField(max_digits=9, decimal_places=6)
    longitude          = models.DecimalField(max_digits=9, decimal_places=6)


    
    #timestamps
    created_date       = models.DateTimeField(auto_now_add=True)
    modified_date      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class ClientListOutside(models.Model):
    class Meta:
        verbose_name_plural = "Client List North East and beyond"


    name               = models.CharField(max_length=100, null=True, blank=True)
    location_name      = models.CharField(max_length=100, null=True, blank=True)
    latitude           = models.DecimalField(max_digits=9, decimal_places=6)
    longitude          = models.DecimalField(max_digits=9, decimal_places=6)


    
    #timestamps
    created_date       = models.DateTimeField(auto_now_add=True)
    modified_date      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)