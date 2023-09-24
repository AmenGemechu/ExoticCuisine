from django.contrib import admin
from .models import Bookings, Users, Test2, Test3
from .models import Reservation

# Register your models here.


admin.site.register(Bookings)
admin.site.register(Users)
admin.site.register(Test2)
admin.site.register(Test3)
admin.site.register(Reservation)
