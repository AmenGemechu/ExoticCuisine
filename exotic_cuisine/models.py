from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from cloudinary.models import CloudinaryField  # not needed anymore

# crud


class exotic_cuisine(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(null=True)
    authour = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='exotic_cuisine')
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)


# get url of a post
def get_absolute_url(self):
    return reverse('exotic_cuisine:single', args=[self.slug])


# new post at the top
class Meta:
    ordering = ['-published']


# display title instead of object
def __str__(self):
    return self.title


# D
# class Bookings(models.Model):
  #  username = models.CharField(max_length=50)
  #  table_id = models.IntegerField(null=False)
  #  bdate = models.DateTimeField()
  #  timeslot = models.IntegerField(null=False)


# class Users(models.Model):
  #  firstname = models.CharField(max_length=20)
  #  laststname = models.CharField(max_length=20)


# class Test2(models.Model):
#    username2 = models.CharField(max_length=50)
 #   table_id2 = models.IntegerField(null=False)
 #   bdate2 = models.DateTimeField()
 #   timeslot2 = models.IntegerField(null=False)


# class Test3(models.Model):
 #   username3 = models.CharField(max_length=50)
 #   table_id3 = models.IntegerField(null=False)
 #   bdate3 = models.DateTimeField()
 #   timeslot3 = models.IntegerField(null=False)


# class Reservation(models.Model):
   # template_name = "reservation.html"

   # def post(self, request):
    #   fname = request.POST.get("fname")
    #  lname = request.POST.get("fname")
    #   email = request.POST.get("email")
    #  message = request.POST.get("request")

    #  reservation = Reservation.objects.create(
    #       first_name=fname,
    #       last_name=lname,
    #       email=email,
    #      request=message,
    #  )

    #   reservation.save()

    #   messages.add_message(request, messages.SUCCESS,
    #                        f"Thanks {fname} for making an reservation!")
    #    return HttpResponseRedirect(request.path)


# def __str__(self):
   # return self.username
