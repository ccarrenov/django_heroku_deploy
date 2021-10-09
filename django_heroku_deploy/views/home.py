from django.http import HttpResponse, HttpRequest

def home(request):
    #return HttpResponse('HOME PAGE.')
    print('home')
    return render(request, 'index.html')
