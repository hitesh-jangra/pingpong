import logging
from django.shortcuts import render
from django.http import HttpResponse

log = logging.getLogger('first')

# Create your views here.

def home_view(request):
    log.info(f'Home view is called')
    return HttpResponse('<h1>This is home page of the ping-pong application</h1>')

def ping_view(request):
    log.info(f'Ping view is called')
    return HttpResponse('<h1>PONG</h1>')