from django.contrib import admin
from .models import Video

# Videos admin panel 

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rx_title', 'is_published', 'list_date',)
    list_display_links = ('id', 'title')
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    search_fields = ('id','title' 'rx_title',)
    list_per_page = 50

admin.site.register(Video, VideoAdmin)