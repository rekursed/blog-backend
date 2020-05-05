from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog import views
app_name = 'blog'

urlpatterns = [
    path('', views.index),
]