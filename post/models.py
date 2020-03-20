from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Post(models.Model):
    title = models.CharField(_("Blog Title"), max_length=50)
    image = models.FileField(_("Blog Image"), upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)