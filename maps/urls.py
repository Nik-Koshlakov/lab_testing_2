from django.conf.urls import patterns, url
from maps.views import index_view, control_view

__author__ = 'max'


urlpatterns = patterns(
    '',
    url(r'^$', index_view, name='index'),
    url(r'^map-control/(?P<map_id>\d+)/$', control_view, name='control'),
)
