from django.contrib import admin
from .models import Video
from msigana_ecommerce.admin_site import admin_site


class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'mobile_video_url', 'tablet_video_url', 'desktop_video_url']

admin_site.register(Video, VideoAdmin)


