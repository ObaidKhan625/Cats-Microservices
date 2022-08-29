from django.shortcuts import render
import random
import requests
import json
# Create your views here.

def index(request):
    return render(request, 'index.html')

def get_cat_photos_service_1(request):
    print("HELLO")
    url = "http://172.22.0.5:8000/"
    r = requests.get(url)
    data = json.loads(r.text)
    context = {'cat_photo_url': data['url']}
    print(data['url'])
    return render(request, 'cat_photos.html', context)

def get_cat_photos_service_2(request):
    url = "http://172.22.0.4:8000/"
    r = requests.get(url)
    data = json.loads(r.text)
    context = {'cat_photo_url': data['url']}
    print(data['url'])
    return render(request, 'cat_photos.html', context)

def get_cat_photos_service_3(request):
    url = "http://172.22.0.3:8000/"
    r = requests.get(url)
    data = json.loads(r.text)
    context = {'cat_photo_url': data['url']}
    print(data['url'])
    return render(request, 'cat_photos.html', context)



