# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

import random
import string

from shortener.settings import SITE_URL

from urlparse import urlparse, urljoin

# Create your models here.

SHORT_CODE_LENGTH = 6


class Url(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=6)

    def __unicode__(self):
        return self.original_url

    def get_short_url(self):
        return SITE_URL + self.short_code


@receiver(pre_save, sender=Url)
def url_pre_save_callback(sender, instance, *args, **kwargs):
    remaining_url = None
    parsed_url = urlparse(instance.original_url)
    netloc = parsed_url.netloc
    if 'www.' in netloc:
        netloc = netloc.split('www.')[1]
    if len(instance.original_url.split(netloc)) > 2:
        remaining_url = instance.original_url.split(netloc)[3]
    instance.original_url = 'https://' + netloc
    if remaining_url:
        instance.original_url = instance.original_url + remaining_url

    if not instance.short_code and not Url.objects.filter(original_url=instance.original_url).exists():
        while True:
            short = ''.join(random.SystemRandom().choice(
                            string.ascii_uppercase +
                            string.ascii_lowercase +
                            string.digits)
                            for _ in xrange(SHORT_CODE_LENGTH))
            if not Url.objects.filter(short_code=short).exists():
                break
    else:
        url = Url.objects.filter(original_url=instance.original_url).first()
        short = url.short_code
    instance.short_code = short
