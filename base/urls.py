from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='register-home'),
    path('lobby/', views.lobby, name='base-lobby'),
    path('room/', views.room, name='base-room'),
    path('get_token/', views.getToken, name='base-getToken'),
    path('create_member/', views.createMember, name='base-createMember'),
    path('get_member/', views.getMember, name='base-getMember'),
    path('delete_member/', views.deleteMember, name='base-deleteMember'),

]
