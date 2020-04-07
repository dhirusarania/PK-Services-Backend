from django.db import models
from django.conf import settings

# Create your models here.
class CareerQuery(models.Model):
    class Meta:
        verbose_name_plural = "Career Query"


    name               = models.CharField(max_length=100, null=True, blank=True)
    email              = models.EmailField(verbose_name='email address', max_length=255, unique=False)
    phone_number       = models.CharField( max_length=17, unique=False)
    address            = models.TextField ( blank=True)
    files              = models.FileField(upload_to = settings.MEDIA_URL_IMG_FIELD, blank=True)
    
    #timestamps
    created_date       = models.DateTimeField(auto_now_add=True)
    modified_date      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class ContactUs(models.Model):
    class Meta:
        verbose_name_plural = "Contact Us"


    name               = models.CharField(max_length=100, null=True, blank=True)
    email              = models.EmailField(verbose_name='email address', max_length=255, unique=False)
    subject            = models.CharField( max_length=255, blank=True, null=True)
    message            = models.TextField ( blank=True)
    
    #timestamps
    created_date       = models.DateTimeField(auto_now_add=True)
    modified_date      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)