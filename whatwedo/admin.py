from django.contrib import admin
from .models import pksercurity, pkservices


class homepage(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    list_display_links = ('title','content',)
    ordering = ('id',)


# Register your models here.
admin.site.register(pksercurity, homepage)
admin.site.register(pkservices, homepage)