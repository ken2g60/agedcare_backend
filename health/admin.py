from django.contrib import admin

from .models import HealthData, Glucose, Pressure, Weight


class HealthAdmin(admin.ModelAdmin):
    list_display = ('userId', 'phonenumber', 'bloodsugar', 'bloodpressure', 'bloodcholesterol', 'bloodlevel', 'weight', 'created_at')

class GlucoseAdmin(admin.ModelAdmin):
    list_display = ('userId', 'glucose', 'created_at')

class PressureAdmin(admin.ModelAdmin):
    list_display = ('userId', 'systolic', 'diastolic', 'created_at')


class WeightAdmin(admin.ModelAdmin):
    list_display = ('userId', 'weight')

    
    
admin.site.register(HealthData, HealthAdmin)
admin.site.register(Glucose, GlucoseAdmin)
admin.site.register(Pressure, PressureAdmin)
admin.site.register(Weight, WeightAdmin)