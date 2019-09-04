from django.contrib import admin
from django.urls import path
from.views import signup,Login
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('signup/',signup ,name='signup'),
    path('login/',Login.as_view() ,name='login'),
    path('logout/',LogoutView.as_view() ,name='logout'),
]