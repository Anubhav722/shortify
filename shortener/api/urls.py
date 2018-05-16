from django.conf.urls import url

from api import views

app_name = 'api'
urlpatterns = [
    url(r'^original/$', views.OriginalUrlView.as_view(), name='original'),
    url(r'^urllist/$', views.UrlListView.as_view()),
    url(r'^redirect/(?P<short_id>[0-9]+)/$', views.url_redirect, name='redirect'),
    url(r'^shortit/$', views.UrlFormView.as_view(), name='form'),
    url(r'^upload_bulk/$', views.BulkUploadView.as_view(), name=  'bulk'),
]
