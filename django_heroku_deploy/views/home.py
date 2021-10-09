from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def home(request):
    #return HttpResponse('HOME PAGE.')
    print('home')
    return render(request, 'index.html')
