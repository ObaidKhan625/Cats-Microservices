from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json
import os
# Create your views here.

catPhotoUrl = None

class CatPhotoSerializer(serializers.Serializer):
    url = serializers.CharField()

@api_view(['GET'])
def index(request):
    global catPhotoUrl
    if not catPhotoUrl:
        url ="https://api.thecatapi.com/v1/images/search?api_key=YOUR_API_KEY"
        r = requests.get(url)
        data = json.loads(r.text)
        catPhoto = {'url': data[0]['url']}
        catPhotoUrl = CatPhotoSerializer(catPhoto).data
    return Response(catPhotoUrl)