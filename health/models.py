from django.db import models
from django.utils.translation import gettext as _
from careapp.models import UserModel


# Create your models here.
class HealthData(models.Model):
    userId = models.CharField(_("User ID"), max_length=50, null=True, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    phonenumber = models.CharField(_("Phone Number"), max_length=50)
    bloodsugar = models.CharField(_("Blood Sugar"), max_length=50)
    bloodpressure = models.CharField(_("Blood Pressure"), max_length=50)
    bloodcholesterol = models.CharField(_("Blood Cholesterol"), max_length=50)
    bloodlevel = models.CharField(_("Blood level (Hemoglobin)"), max_length=50)
    weight = models.CharField(_("Weight"), max_length=50)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)


class Glucose(models.Model):
    username = models.CharField(_("UserName"), max_length=50)
    glucose = models.CharField(_("Glucose"), max_length=50)
    date = models.CharField(_("Date"), max_length=50)
    time = models.CharField(_("Time"), max_length=50)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)


class Pressure(models.Model):
    username = models.CharField(_("UserName"), max_length=50)
    systolic = models.CharField(_("Systolic"), max_length=50)
    diastolic = models.CharField(_("Diastolic"), max_length=50)
    date = models.CharField(_("Date"), max_length=50)
    time = models.CharField(_("Time"), max_length=50)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)

class Weight(models.Model):
    username = models.CharField(_("UserName"), max_length=50)
    weight = models.CharField(_("Weight"), max_length=50)
    date = models.CharField(_("Date"), max_length=50)
    time = models.CharField(_("Time"), max_length=50)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)
    