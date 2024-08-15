from django.contrib import admin
from .models import Reservation
from msigana_ecommerce.admin_site import admin_site


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date', 'time', 'meal', 'number_of_person', 'email', 'phone')
    list_filter = ('date', 'meal')
    search_fields = ('full_name', 'email', 'phone')
admin_site.register(Reservation, ReservationAdmin)