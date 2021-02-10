from django.contrib import admin
from django.urls import path
from . import  views
urlpatterns = [
    path('',views.Home,name = 'Home' ),
    path('registration/',views.Registration,name = 'Registration' ),
    path('login/',views.Login,name = 'Login' ),
]
