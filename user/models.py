from django.db import models

from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from user.manager import CustomUserManager


from django.db.models.signals import pre_save
from utils.helpers import random_generate 



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