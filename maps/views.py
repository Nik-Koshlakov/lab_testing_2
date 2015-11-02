from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.template import RequestContext


def index_view(request):
    if request.method == 'GET':
        template_name = 'maps/index.html'
        context = RequestContext(request, {})
        return render(request, template_name, context)
    else:
        return HttpResponseNotAllowed(permitted_methods=['get'])
