from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from django.urls import timezone
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


#  Post Model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)  # ecending order
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


#  Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)  # scending order
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


# crud (old)
class exotic_cuisine(models.Model):
    title = models.CharField(max_length=200)  # post
    excerpt = models.TextField(null=True)
    authour = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='exotic_cuisine')  # connecting user to post
    slug = models.SlugField(max_length=100, unique=True)
    update = models.DateTimeField(auto_now=True)  # last post
   # published = models.DateTimeField(default=timezone.now)


# get url of a post
def get_absolute_url(self):
    return reverse('exotic_cuisine:single', args=[self.slug])


# new post at the top
class Meta:
    ordering = ['-published']


# display title instead of object
def __str__(self):
    return self.title


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


# class Reservation(models.Model):
#    template_name = "reservation.html"

#    def post(self, request):
#        fname = request.POST.get("fname")
#        lname = request.POST.get("fname")
#        email = request.POST.get("email")
#        message = request.POST.get("request")

 #   reservation = Reservation.objects.create(
 #       first_name=fname,
 #       last_name=lname,
 #       email=email,
 #       request=message,
 #   )

 #   reservation.save()

 #   messages.add_message(request, messages.SUCCESS,
 #                        f"Thanks {fname} for making an reservation!")
    # return HttpResponseRedirect(request.path)


def __str__(self):
    return self.username
