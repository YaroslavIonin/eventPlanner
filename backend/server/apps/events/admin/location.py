from django.contrib import admin
from django_admin_geomap import ModelAdmin

from ..models import Location, Event


class EventInstanceInline(admin.TabularInline):
    model = Event
    fields = ('main_name', 'owner')


@admin.register(Location)
class LocationAdmin(ModelAdmin):
    list_display = ('address',)
    geomap_field_longitude = "id_longitude"
    geomap_field_latitude = "id_latitude"
    inlines = (EventInstanceInline, )
    geomap_default_longitude = "60.6122"
    geomap_default_latitude = "56.8519"
    geomap_default_zoom = "11"
    # geomap_show_map_on_list = False
    # geomap_height = "300px"
