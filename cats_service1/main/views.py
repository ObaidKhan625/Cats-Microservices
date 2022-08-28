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

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@api_view(['GET'])
def index(request):
    print(get_client_ip(request))
    global catPhotoUrl
    if not catPhotoUrl:
        url ="https://api.thecatapi.com/v1/images/search?api_key=YOUR_API_KEY"
        r = requests.get(url)
        data = json.loads(r.text)
        catPhoto = {'url': data[0]['url']}
        catPhotoUrl = CatPhotoSerializer(catPhoto).data
    return Response(catPhotoUrl)