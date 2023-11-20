from . import views
# from django. http import HttpResponse
from django.urls import path


app_name = 'exotic_cuisine'

# are read top to bottom
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('register/', views.registerPage, name='register'),
    path('login_user/', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    # path('', views.IndexView.as_view(), name='index'),
    # path('add/', views.AddView.as_view(), name='add'),
    # path('posts/', views.PostsView.as_view(), name='posts'),
    # path('<slug:slug>/', views.SingleView.as_view(), name='single'),
    # path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
]
