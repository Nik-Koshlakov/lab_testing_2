from django.contrib import admin
from maps.models import City, Distance, Map

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'coord_X', 'coord_Y', 'map')

admin.site.register(City, CityAdmin)
admin.site.register(Distance)
admin.site.register(Map)
