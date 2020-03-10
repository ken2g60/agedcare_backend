from django.contrib import admin

from .models import PersonalDetail , UserModel, ClaimsModel, ContributionModel

class UserAdmin(admin.ModelAdmin):
    list_display = ('userId', 'fullname', 'phonenumber', 'gender', 'balance', 'created_at')
    
    
    
class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth',  'height', 'occupation', 'sector', 'region', 'created_at')




class ClaimsModelAdmin(admin.ModelAdmin):
    list_display = ('userId', 'amount_withdraw', 'purpose', 'facility_attended', 'date_attended', 'created_at')


class ContributionModelAdmin(admin.ModelAdmin):
    list_display = ('userId', 'momo', 'amount', 'month', 'created_at')

admin.site.register(PersonalDetail, PersonalDetailAdmin)
admin.site.register(UserModel, UserAdmin)
admin.site.register(ClaimsModel, ClaimsModelAdmin)
admin.site.register(ContributionModel, ContributionModelAdmin)