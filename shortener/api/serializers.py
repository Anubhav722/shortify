from rest_framework import serializers

from api.models import Url


class UrlSerializer(serializers.ModelSerializer):
    short_code = serializers.CharField(required=False, source='get_short_url')

    class Meta:
        model = Url
        fields = ('id', 'original_url', 'short_code')


class ShortUrlSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(required=True)

    class Meta:
        model = Url
        fields = ('id', 'short_url')
