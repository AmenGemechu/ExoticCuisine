from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Bookings(models.Model):
    username = models.CharField(max_length=50)
    table_id = models.IntegerField(null=False)
    bdate = models.DateTimeField()
    timeslot = models.IntegerField(null=False)


class Users(models.Model):
    firstname = models.CharField(max_length=20)
    laststname = models.CharField(max_length=20)
