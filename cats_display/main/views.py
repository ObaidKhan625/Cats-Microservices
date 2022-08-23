from django.shortcuts import render
import random
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def get_cat_photos(request):
    url = "http://127.0.0.1:8001/"
    r = requests.get(url)
    data = json.loads(r.text)
    context = {'cat_photo_url': data['url']}
    return render(request, 'cat_photos.html', context)