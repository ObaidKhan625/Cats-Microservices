from django.shortcuts import render
import random
import requests
import json
import os

catsList = []

# Create your views here.
def index(request):
    return render(request, 'index.html')

def get_cat_photos(request):
    global catsList
    if(len(catsList) < 3):
        url ="https://api.thecatapi.com/v1/images/search?api_key=YOUR_API_KEY"
        r = requests.get(url)
        data = json.loads(r.text)
        catsList.append(data[0]['url'])
    context = {'cat_photo_url': random.choice(catsList)}
    return render(request, 'cat_photos.html', context)