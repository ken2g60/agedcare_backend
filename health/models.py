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