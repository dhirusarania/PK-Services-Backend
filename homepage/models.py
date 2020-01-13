from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

# Create your models here.
class HomepageSlider(models.Model):
    class Meta:
        verbose_name_plural = "Homepage Slider Images"


    title               = models.CharField(max_length=100, null=True, blank=True)
    image               = models.ImageField(upload_to = settings.MEDIA_URL_IMG_FIELD)

    
    #timestamps
    created_date       = models.DateTimeField(auto_now_add=True)
    modified_date      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = "Testimonial"


    name                 = models.CharField(max_length=50, null=False, blank=False)
    user_type            = models.CharField(max_length=50, null=False, blank=False, default='Client')
    image                = models.ImageField(upload_to = settings.MEDIA_URL_IMG_FIELD)
    testimonial          = models.TextField(blank=False)

    
    #timestamps
    created_date       = models.DateTimeField(auto_now_add=True)
    modified_date      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)