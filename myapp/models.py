from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings



class seats(models.Model):
    CHOICES = (
        ('allow', 'Allow'),
        ('occupied', 'Occupied'),
    )
    slot_name = models.CharField(max_length=50, blank=True, null=True)
    visiname = models.CharField(max_length=50, blank=True, null=True, default="NONE")
    date = models.DateTimeField(default=datetime.now, blank=True)
    status =  models.CharField(max_length=50, choices= CHOICES, blank=True, default = "allow")





class allbookings(models.Model):
    CHOICES = (
        ('allow', 'Allow'),
        ('occupied', 'Occupied'),
    )
    slot_name = models.CharField(max_length=50, blank=True, null=True)
    visiname = models.CharField(max_length=50, blank=True, null=True, default="NONE")
    date = models.DateTimeField(default=datetime.now, blank=True)
    status =  models.CharField(max_length=50, choices= CHOICES, blank=True, default = "allow")
