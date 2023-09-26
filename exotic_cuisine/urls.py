from django.urls import path
from . import views


app_name = 'exotic_cuisine'

# are read top to bottom
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('<slug:slug>/', views.SingleView.as_view(), name='single'),
]
