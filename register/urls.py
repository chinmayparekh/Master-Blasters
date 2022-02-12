from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='register-home'),
    path('signUpRecruiter', views.register_rec, name='register-rec'),
    path('signUpPCell', views.register_cell, name='register-cell'),
    path('profile',views.profile,name='register-profile'),
]

