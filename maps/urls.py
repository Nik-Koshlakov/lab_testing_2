from django.conf.urls import patterns, url
from maps.views import index_view

__author__ = 'max'


urlpatterns = patterns(
    '',
    url(r'^$', index_view, name='index'),
)
