from django.shortcuts import render


def get_base(request):
    return render(request, 'exotic_cuisine/base.html')


def get_home(request):
    return render(request, 'exotic_cuisine/home.html')
