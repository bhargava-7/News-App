from django.contrib import admin
from django.urls import path

from . import views
from django.urls import include, path

app_name = 'login'
urlpatterns = [
    path('login/', views.login_page, name="loginhome"),
    path('signup/', views.sign_up, name="signuphome"),
    path('profile/', views.profile, name="profile"),
    path('logout/',views.logout_user,name="logout"),
    
]
