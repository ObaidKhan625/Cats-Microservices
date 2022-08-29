from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json
import os
import random
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.conf import settings
from datetime import datetime, timedelta
# Create your views here.

class CatPhotoSerializer(serializers.Serializer):
    url = serializers.CharField()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return str(ip)

@api_view(['GET'])
def index(request):
    currIp = get_client_ip(request)
    apiList = cache.get('call-rate-'+currIp)
    if(not apiList):
        cache.set('call-rate-'+currIp, [])
        cache.expire_at('call-rate'+currIp, datetime.now() + timedelta(minutes=3))
    if len(apiList) < 5 :
        url ="https://api.thecatapi.com/v1/images/search?api_key=YOUR_API_KEY"
        r = requests.get(url)
        data = json.loads(r.text)
        catPhoto = {'url': data[0]['url']}
        catPhotoUrl = CatPhotoSerializer(catPhoto).data
        apiList.append(catPhotoUrl)
        cache.set('call-rate-'+currIp, apiList)
    else:
        catPhotoUrl = random.choice(apiList)
    return Response(catPhotoUrl)

