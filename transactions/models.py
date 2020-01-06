from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Deposit(models.Model):
    momo = models.CharField(_("Mobile Money"), max_length=50)
    amount = models.CharField(_("Amount"), max_length=50)
    txtRef = models.CharField(_("Reference"), max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)

class Withdraw(models.Model):
    momo = models.CharField(_("Mobile Money"), max_length=50)
    amount = models.CharField(_("Amount"), max_length=50)
    txtRef = models.CharField(_("Reference"), max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)

class TransactionHistory(models.Model):
    momo = models.CharField(_("Mobile Money"), max_length=50)
    amount = models.CharField(_("Amount"), max_length=50)
    txtRef = models.CharField(_("Reference"), max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)