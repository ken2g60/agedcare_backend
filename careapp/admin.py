from django.contrib import admin

from .models import HealthData, PersonalDetail , UserModel

class HealthAdmin(admin.ModelAdmin):
    list_display = ('userId', 'phonenumber', 'bloodsugar', 'bloodpressure', 'bloodcholesterol', 'bloodlevel', 'weight', 'created_at')


class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = ('date_of_birth',  'height', 'occupation', 'sector', 'region')


class UserAdmin(admin.ModelAdmin):
    list_display = ('userId', 'fullname', 'phonenumber', 'gender', 'created_at')

admin.site.register(HealthData, HealthAdmin)
admin.site.register(PersonalDetail, PersonalDetailAdmin)
admin.site.register(UserModel, UserAdmin)