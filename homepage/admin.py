from django.contrib import admin
from .models import HomepageSlider


class homepage(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    list_display_links = ('title','image',)
    ordering = ('id',)


# Register your models here.
admin.site.register(HomepageSlider, homepage)