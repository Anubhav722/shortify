from __future__ import absolute_import
from celery.decorators import task

import re

from api.models import Url


@task(name='parse_csv_file')
def parse_csv(file):
    new_str = re.sub(r'\s+', ' ', file).replace(' ', '')
    for url in new_str.split(','):
        Url.objects.create(original_url=url)
