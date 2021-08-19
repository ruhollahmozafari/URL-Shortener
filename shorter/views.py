import re
from rest_framework import serializers
from shorter.models import Url
from shorter.serializers import LongUrlsSerializer, ShortUrlsSerializer
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions, status, viewsets  
from django.http import HttpResponseRedirect , HttpResponsePermanentRedirect


from .serializers import *


class CreateShortUrl(generics.CreateAPIView):
    serializer_class = FullUrlsSerializer
    queryset = Url.objects.all()

class GetShortUrl(generics.RetrieveAPIView):
    serializer_class = FullUrlsSerializer
    lookup_field = 'long'
    queryset = Url.objects.all()

def redirect_to_long(request, *args, **kwargs):
    short = 'http://localhost:8000/r/' + kwargs['string'] + '/'
    url_object = Url.objects.get(short = short)
    url_object.visit_number += 1 
    url_object.save()
    return redirect(url_object.long)



