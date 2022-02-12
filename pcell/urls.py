from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_posts/', views.view_posts, name='view_posts'),
    # path('filter_posts/', views.filter_posts, name='filter_posts'),
    
]