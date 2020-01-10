from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import ClientListKamrup, ClientListOutside

admin.site.site_header = "PK Services Admin"
admin.site.site_title = "PK Services Admin Portal"
admin.site.index_title = "Welcome to PK Services Portal"


class client_list(admin.ModelAdmin):
    list_display = ('id', 'name', 'location_name' ,'latitude', 'longitude')
    list_display_links = ('name',)
    ordering = ('id',)


# Register your models here.
admin.site.register(ClientListKamrup, client_list)
admin.site.register(ClientListOutside, client_list)

admin.site.unregister(Group)
admin.site.unregister(User)