from .models import exotic_cuisine  # crud
from django.views.generic import ListView, DeleteView, UpdateView, CreateView  # crud
from django.urls import reverse_lazy  # crud
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout  # crud remove authenticate
from .forms import PostForm, CreateUserForm
from django.contrib import messages


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
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    context = {}
    return render(request, 'login.html', context)
