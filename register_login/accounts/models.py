import email
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    subject=models.CharField(max_length=50)
    message=models.TextField()



class DTModel(models.Model):
    name = models.CharField(max_length=64, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    date_time = models.DateTimeField(null=True)