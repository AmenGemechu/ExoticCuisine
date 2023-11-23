from .models import Comment
from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import exotic_cuisine
from django import forms
from django.contrib.auth.models import User


# new
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = exotic_cuisine
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
