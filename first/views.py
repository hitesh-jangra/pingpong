from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse('<h1>This is home page of the ping-pong application</h1>')

def ping_view(request):
    return HttpResponse('<h1>PONG</h1>')