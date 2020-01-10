from django.contrib import admin
from .models import CareerQuery, ContactUs

# Register your models here.
class CareerQuery_field(admin.ModelAdmin):
    list_display = ('id', 'name', 'email' ,'phone_number', 'address', 'files')
    list_display_links = ('name', 'email' ,'phone_number')
    ordering = ('-id',)

# Register your models here.
class ContactUs_field(admin.ModelAdmin):
    list_display = ('id', 'name', 'email' , 'subject', 'message')
    list_display_links = ('name', 'email')
    ordering = ('-id',)


# Register your models here.
admin.site.register(CareerQuery, CareerQuery_field)
admin.site.register(ContactUs, ContactUs_field)