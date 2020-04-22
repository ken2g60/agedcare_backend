from django.db import models
from django.utils.translation import gettext as _

class Post(models.Model):
    title = models.CharField(_("Blog Title"), max_length=50)
    image = models.FileField(_("Blog Image"), upload_to='images/')
    description = models.TextField(blank=True)
    posted_time = models.DateField(_("Posted Date"), auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)