from django.contrib import admin
from .models import Event
from msigana_ecommerce.admin_site import admin_site


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date')
    search_fields = ('title',)

admin_site.register(Event , EventAdmin)