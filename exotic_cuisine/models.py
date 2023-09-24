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


class Test2(models.Model):
    username2 = models.CharField(max_length=50)
    table_id2 = models.IntegerField(null=False)
    bdate2 = models.DateTimeField()
    timeslot2 = models.IntegerField(null=False)


class Test3(models.Model):
    username3 = models.CharField(max_length=50)
    table_id3 = models.IntegerField(null=False)
    bdate3 = models.DateTimeField()
    timeslot3 = models.IntegerField(null=False)


class Reservation(models.Model):
    template_name = "reservation.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("fname")
        email = request.POST.get("email")
        message = request.POST.get("request")

        reservation = Reservation.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            request=message,
        )

        reservation.save()

        messages.add_message(request, messages.SUCCESS,
                             f"Thanks {fname} for making an reservation!")
        return HttpResponseRedirect(request.path)


def __str__(self):
    return self.username
