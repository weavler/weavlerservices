from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm


class DemoProduct(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    image = models.ImageField("Image", upload_to="images/")
