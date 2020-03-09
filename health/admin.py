from django.contrib import admin

from .models import HealthData

# Register your models here.
class HealthAdmin(admin.ModelAdmin):
    list_display = ('userId', 'phonenumber', 'bloodsugar', 'bloodpressure', 'bloodcholesterol', 'bloodlevel', 'weight', 'created_at')

admin.site.register(HealthData, HealthAdmin)
