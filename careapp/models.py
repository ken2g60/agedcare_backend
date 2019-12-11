from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class PersonalDetail(models.Model):

    gender_options = (
        ('Select an option', 'Select an option'),
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    lanuage_options = (
        ('Select an option', 'Select an option'),
        ('First Lanauage', 'First Lanuage'),
        ('Second Lanauage', 'Second Lanauage')
    )
    sector_options = (
        ('Select an option', 'Select an option'),
        ('Public Sector', 'Public Sector'),
        ('Private Sector', 'Private Sector')
    )

    pension_options = (
        ('Select an option', 'Select an option'),
        ('Social Security', 'Social Security'),
        ('Other', 'Other')
    )
    name = models.CharField(_("Name"), max_length=50)
    date_of_birth = models.CharField(_("Date of birth"), max_length=50)
    gender = models.CharField(_("Gender"), max_length=50, choices=gender_options, default=gender_options[0][0])
    height = models.CharField(_("Height"), max_length=50)
    occupation = models.CharField(_("Occupation"), max_length=50)
    sector = models.CharField(_("Sector"), max_length=50, choices=sector_options, default=sector_options[0][0])
    region = models.CharField(_("Region"), max_length=250)
    municipality_district = models.CharField(_("Municipality / District"), max_length=50)
    town = models.CharField(_("Town"), max_length=50)
    residential_address = models.CharField(_("Residential Address"), max_length=50)
    number_of_years_service = models.CharField(_("Number of years in service"), max_length=50)
    number_dependents = models.CharField(_("Number Dependents"), max_length=50)
    registered_nhis =  models.BooleanField(_("Registered with NHIS"), default=False)
    private_health = models.BooleanField(_("Registered with any private health insurance?"), default=False)
    pension_scheme = models.CharField(_("Pension Scheme"), max_length=50)
    userId = models.CharField(_("Unique ID"), max_length=50)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)



class HealthData(models.Model):
    userId = models.CharField(_("Unique ID"), max_length=50)
    bloodglucose = models.CharField(_("Blood Glucose"), max_length=50)
    bloodpressure = models.CharField(_("Blood Pressure"), max_length=50)
    bloodcholesterol = models.CharField(_("Blood Cholesterol"), max_length=50)
    bloodlevel = models.CharField(_("Blood level (Hemoglobin)"), max_length=50)
    weight = models.CharField(_("Weight"), max_length=50)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)


class ContributionModel(models.Model):
    userId = models.CharField(_("Unique ID"), max_length=50)
    amount = models.CharField(_("Amount"), max_length=50)
    month = models.CharField(_("Month"), max_length=50)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)


class ClaimsModel(models.Model):
    userId = models.CharField(_("Unique ID"), max_length=50)
    amount_withdraw =  models.CharField(_("Withdraw"), max_length=50)
    purpose =  models.CharField(_("Purpose"), max_length=50)
    facility_attended = models.CharField(_("Facility Attended"), max_length=50)
    date_attended = models.CharField(_("Facility Attended"), max_length=50)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)