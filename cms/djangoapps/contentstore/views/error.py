from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound

from mitxmako.shortcuts import render_to_string, render_to_response


def not_found(request):
    return render_to_response('error.html', {'error': '404'})


def server_error(request):
    return render_to_response('error.html', {'error': '500'})


def render_404(request):
    return HttpResponseNotFound(render_to_string('404.html', {}))


def render_500(request):
    return HttpResponseServerError(render_to_string('500.html', {}))


