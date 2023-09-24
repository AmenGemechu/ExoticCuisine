from django.shortcuts import render
from .models import Bookings
from .models import Reservation


def get_base(request):
    return render(request, 'home.html')


def allbookings(request):
    bookings = Bookings.objects.all()
    return render(request, 'test.html',
                  {'bookings': bookings})
