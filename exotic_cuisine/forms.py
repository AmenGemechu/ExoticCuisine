from django import forms
from .models import exotic_cuisine


class PostForm(forms.ModelForm):
    class Meta:
        model = exotic_cuisine
        fields = "__all__"
