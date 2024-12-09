from django.contrib import admin
from django.urls import path, include
from .views import home_view, ping_view

urlpatterns = [
    path('', home_view),
    path('ping/', ping_view),
]