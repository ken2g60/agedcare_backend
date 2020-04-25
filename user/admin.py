from django.contrib import admin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('userId','phonenumber', 'email', 'balance', 'is_active', 'is_staff', 'is_superuser', 'created_at')
    
    
admin.site.register(CustomUser, CustomUserAdmin)