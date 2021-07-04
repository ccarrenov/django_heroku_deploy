from django.http import HttpResponse, HttpRequest

def home(request):
    return HttpResponse('HOME PAGE.')
