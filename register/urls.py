from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='register-home'),
    path('signUpRecruiter', views.register_rec, name='register-cell'),
    path('signUpPCell', views.register_cell, name='register-rec'),

]

