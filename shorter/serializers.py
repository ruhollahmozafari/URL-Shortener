from rest_framework import serializers
from .models import *
import string , random
from urllib.parse import urlparse

def long_to_short(long):
    parse_object = urlparse(long)
    random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=5))
    netloc = str(parse_object.netloc)
    scheme = parse_object.scheme
    return  'http://localhost:8000/r/' + random_string + '/'

class LongUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('long',)

class FullUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('long', 'short')
        read_only_fields = ('short',)
        extra_kwargs = {
            'long': {'write_only': True},
        }

    def create(self, validated_data):
        url = Url.objects.create(long = validated_data['long'] , short = long_to_short(validated_data['long']) )
        url.save
        return url



class ShortUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('short',)



     