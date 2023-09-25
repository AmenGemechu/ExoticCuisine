from django.contrib import admin  # crud
from django.urls import path, include  # crud
#from exotic_cuisine.views import get_base
#from django.conf.urls.static import static
#from django.conf import settings
#from exotic_cuisine import views


urlpatterns = [
    path('admin/', admin.site.urls),  # crud
    path('', include('exotic_cuisine.urls', namespace='exotic_cuisine')),  # crud
    # path('', get_base, name='get_base'),
    # path('test', views.allbookings, name='test'),
]
