from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^original/$', views.OriginalUrlView.as_view(), name='original')
]
