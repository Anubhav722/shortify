# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from shortener.settings import SITE_URL
from api.serializers import UrlSerializer, ShortUrlSerializer
from api.models import Url

# Create your views here.


class ShortenerViewSet(mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):

    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class OriginalUrlView(generics.GenericAPIView):
    serializer_class = ShortUrlSerializer
    queryset = Url.objects.all()

    def post(self, request, *args, **kwargs):
        """
        Return original url for short url.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            short_url = serializer.data.get('short_url')
            if SITE_URL in short_url:
                short_code = short_url.split(SITE_URL)[1]
                queryset = Url.objects.filter(short_code=short_code)
                if queryset:
                    url_object = queryset.first()
                    return Response(
                        {'status': 'Success',
                         'details': url_object.original_url},
                        status=status.HTTP_200_OK)
                else:
                    return Response(
                        {'status': 'Failed',
                         'details': 'Please check the short url code'},
                        status=status.HTTP_400_BAD_REQUEST)
            return Response(
                {'status': 'Failed',
                 'details': 'Invalid domain name'},
                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {'status': 'Failed',
                 'details': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST)
