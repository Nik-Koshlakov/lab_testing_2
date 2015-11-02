from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from maps.models import Map


def index_view(request):
    if request.method == 'GET':
        template_name = 'maps/index.html'
        context = RequestContext(request, {
            'maps': Map.objects.all()
        })
        return render(request, template_name, context)
    else:
        return HttpResponseNotAllowed(permitted_methods=['get'])


def control_view(request, map_id):
    if request.method == 'GET':
        template_name = 'maps/map.html'

        map_obj = get_object_or_404(Map, id=map_id)
        context = RequestContext(request, {
            'map': map_obj
        })
        return render(request, template_name, context)
    else:
        return HttpResponseNotAllowed(permitted_methods=['get'])
