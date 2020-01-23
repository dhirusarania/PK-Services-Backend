from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import LatestNews, BlogPost

# Register your models here.
class LatestNews_field(SummernoteModelAdmin):
    list_display = ('id', 'title', 'image')
    list_display_links = ('title',)
    ordering = ('-id',)
    summernote_fields = ('body',)



# Register your models here.
admin.site.register(LatestNews, LatestNews_field)
admin.site.register(BlogPost, LatestNews_field)
from django_summernote.utils import get_attachment_model 
admin.site.unregister(get_attachment_model())
