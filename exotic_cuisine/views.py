from django.contrib import messages
from .forms import PostForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
# from .model import exotic_cuisine
from django.views import generic
from .model import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6  # max_post per page


# Posts
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
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
            # Redirect to a success page.

        else:
            # Return an 'invalid login' error message.
            messages.success(
                request, "There was an Error Logingin. Try again..")
            return redirect('exotic_cuisine:login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You are Logged Out!"))
    return redirect('/')
