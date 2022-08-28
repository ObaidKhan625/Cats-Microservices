from django.shortcuts import render
import random
import requests
import json
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.conf import settings
from datetime import datetime, timedelta

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    # cache.set('name', 'Hey')
    # cache.expire_at('name', datetime.now() + timedelta(seconds=30))
    print(cache.get('name'))
    return render(request, 'index.html')

def get_cat_photos_service_1(request):
    url = "http://172.22.0.2:8000/"
    r = requests.get(url)
    data = json.loads(r.text)
    context = {'cat_photo_url': data['url']}
    return render(request, 'cat_photos.html', context)

def get_cat_photos_service_2(request):
    url = "http://172.22.0.3:8000/"
    r = requests.get(url)
    data = json.loads(r.text)
    context = {'cat_photo_url': data['url']}
    return render(request, 'cat_photos.html', context)

def get_cat_photos_service_3(request):
    url = "http://172.22.0.4:8000/"
    r = requests.get(url)
    data = json.loads(r.text)
    context = {'cat_photo_url': data['url']}
    return render(request, 'cat_photos.html', context)



