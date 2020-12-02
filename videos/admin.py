from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'list_date',)
    list_display_links = ('id', 'title')
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    search_fields = ('id','title')
    list_per_page = 50

admin.site.register(Video, VideoAdmin)