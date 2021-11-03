from django.contrib import admin
from django.urls import path


from newsfeed import views
from django.urls import include, path
from django.conf.urls import url

app_name = 'newsfeed'

urlpatterns = [

    path('technology/', views.technology, name="tech"),
    path('lifestyle/', views.lifestyle, name="life"),
    path('sports/', views.sports, name="sport"),
    path('', views.base, name="base"),
]
