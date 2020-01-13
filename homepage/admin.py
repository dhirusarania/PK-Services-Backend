from django.contrib import admin
from .models import HomepageSlider, Testimonial


class homepage(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    list_display_links = ('title','image',)
    ordering = ('id',)

class testimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'testimonial')
    list_display_links = ('name','image', 'testimonial')
    ordering = ('id',)


# Register your models here.
admin.site.register(HomepageSlider, homepage)
admin.site.register(Testimonial, testimonialAdmin)