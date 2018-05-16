from django.conf.urls import url

from api import views

app_name = 'api'
urlpatterns = [
    url(r'^original/$', views.OriginalUrlView.as_view(), name='original'),
    url(r'^urllist/$', views.UrlListView.as_view()),
    url(r'^redirect/(?P<short_id>[0-9]+)/$', views.url_redirect, name='redirect')
]
