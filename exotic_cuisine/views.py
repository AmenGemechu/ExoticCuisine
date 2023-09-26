from .models import exotic_cuisine  # crud
from django.views.generic import ListView, DeleteView, UpdateView
from .models import Reservation
from .models import Bookings
from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.generic.base import TemplateView


# All posts
class IndexView(ListView):
    model = exotic_cuisine
    template_name = 'index.html'
    context_object_name = 'index'


# Single post
class SingleView(DeleteView):
    model = exotic_cuisine
    template_name = 'single.html'
    context_object_name = 'post'


class PostsView(ListView):
    model = exotic_cuisine
    template_name = 'posts.html'
    context_object_name = 'post_list'


# def get_base(request):
 #   return render(request, 'home.html')


# def get_base(request):
 #   return render(request, 'reservation.html')


# def allbookings(request):
 #   bookings = Bookings.objects.all()
  #  return render(request, 'test.html',
   #               {'bookings': bookings})
