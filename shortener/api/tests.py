# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from rest_framework.test import APIRequestFactory
from rest_framework import status

from api.views import ShortenerViewSet as SVS

# Create your tests here.


class ShortUrlGeneratorTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.url_1 = 'https://google.com'
        self.url_2 = 'http://google.com'
        self.url_3 = 'https://www.google.com'

    def test_url_generation_for_identical_url(self):
        request = self.factory.post('/short/', {'original_url': self.url_1})
        response = SVS.as_view({'post': 'create'})(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        short_url_1 = response.data.get('short_code')
        request = self.factory.post('/short/', {'original_url': self.url_2})
        response = SVS.as_view({'post': 'create'})(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        short_url_2 = response.data.get('short_code')

        request = self.factory.post('/short/', {'original_url': self.url_3})
        response = SVS.as_view({'post': 'create'})(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        short_url_3 = response.data.get('short_code')

        self.assertEqual(short_url_1, short_url_2)
        self.assertEqual(short_url_2, short_url_3)
        self.assertEqual(short_url_3, short_url_1)
