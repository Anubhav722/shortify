# shortify

## Endpoints available

API ENDPOINTS
1. /short/ - GET, POST, DELETE (to shorten urls)
2. /shortify/original/ - POST (to view original url from short_url)
3. /shortify/bulk_upload/ - POST (to upload .csv files)

TEMPLATE ENDPOINTS
1. /shortify/urllist/ - GET(to get all the availble short urls)
  Clicking on the short urls redirects user to the original url
  
2. /shortify/shortit/ - POST (input original url to be shortened)

## Initial Requirements and Project Setup

1. Create a virtualenv for python 2
2. Clone the project
3. Install the dependencies ```pip install requirements.txt```

## For bulk upload (.csv files) have used async tasks (celery) and redis as a broker
Make sure redis server is running by
```redis-cli ping```
Should return ```PONG```

To run celery 
``` celery -A shortener worker```

For running django server ```./manage.py runserver```

## Running Tests

Have not covered the code with tests. Idea was to cover the unique urls generator function for identical original urls.
Have omitted those tests, was running low on time.
Run ```./manage.py test```

# NOTE:

url's such as `google.com` and `www.google.com` are not considered valid according to `URLField`.
Validations are being performed by django. Only urls starting with `https` or `http` are considered as urls
