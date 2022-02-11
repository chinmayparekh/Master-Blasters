from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='base-home'),
    path('make_post/', views.make_post, name='make_post'),
    
]