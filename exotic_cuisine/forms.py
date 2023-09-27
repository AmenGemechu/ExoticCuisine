from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import exotic_cuisine
from django import forms
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = exotic_cuisine
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        