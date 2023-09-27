from .models import exotic_cuisine  # crud
from django.views.generic import ListView, DeleteView, UpdateView, CreateView  # crud
from django.urls import reverse_lazy  # crud
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm, CreateUserForm


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


class AddView(CreateView):
    model = exotic_cuisine
    template_name = "add.html"
    fields = '__all__'
    success_url = reverse_lazy('exotic_cuisine:posts')


class EditView(UpdateView):
    model = exotic_cuisine
    template_name = "edit.html"
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('exotic_cuisine:posts')


class DeleteView(DeleteView):
    model = exotic_cuisine
    pk_url_kwarg = 'pk'
    template_name = "confirm-delete.html"
    success_url = reverse_lazy('exotic_cuisine:posts')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'register.html', context)


# def get_base(request):
 #   return render(request, 'home.html')


# def get_base(request):
 #   return render(request, 'reservation.html')


# def allbookings(request):
 #   bookings = Bookings.objects.all()
  #  return render(request, 'test.html',
   #               {'bookings': bookings})
