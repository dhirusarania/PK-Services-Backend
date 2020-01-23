from django.contrib import admin
from .models import job_category, job_opening


class homepage(admin.ModelAdmin):
    list_display = ('id',  'category', 'title')
    list_display_links = ('title','category')
    ordering = ('id',)

# Register your models here.
admin.site.register(job_category)
admin.site.register(job_opening, homepage)