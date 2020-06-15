from django.db import models

from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from user.manager import CustomUserManager


from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from utils.helpers import random_generate 

from datetime import datetime

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    
    userId = models.CharField(_("User ID"), max_length=50)
    phonenumber = models.CharField(_("Phonenumber"), max_length=50, unique=True)
    email = models.CharField(_("Email Address"), max_length=50)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    objects = CustomUserManager()

   
    
    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = []
    

def generate_user_id(instance, sender, *args, **kwargs):
    if not instance.userId:
        instance.userId = random_generate(4)
pre_save.connect(generate_user_id, sender=CustomUser)


class Payment(models.Model):
    amount = models.DecimalField(_("Amount"), max_digits=12, decimal_places=2)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    phonenumber = models.CharField(_("Phone Number"), max_length=50)
    subscription = models.CharField(_("Subscription Type"), max_length=50)
    paid_status = models.BooleanField(_("Payment Status"))
    email = models.CharField(_("Email Address"), max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)




class Subscription(models.Model):

    subscription_status = (
        ('select option', 'select option'),
        ('activate', 'activate'),
        ('deactivate', 'deactivate'),
    )
    
    
    is_active = models.BooleanField(default=False)
    initiated_on = models.DateTimeField(null=True, blank=True)
    terminated_on = models.DateTimeField(null=True, blank=True)
    subscription_type = models.CharField(_("Subscription Type"), max_length=50)
    subscription_status = models.CharField(_("Subscription Status"), max_length=50, default=subscription_status[1][1])
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    
    # update the subscription
    @property
    def get_created_date(self):
        pass
        
    
    @property
    def get_next_billing_date(self):
        pass