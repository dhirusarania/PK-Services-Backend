from django.db import models
from django.conf import settings

# Create your models here.
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