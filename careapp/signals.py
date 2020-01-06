from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import UserModel


# @receiver(pre_save, sender=UserModel)
# def generate_user_id(sender, instance, created, **kwargs):
# 	if created:
# 		instance.userId = random_generate(4)
  