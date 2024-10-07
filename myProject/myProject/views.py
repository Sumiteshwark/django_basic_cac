from django.http import HttpResponse

def Home(request):
    return HttpResponse('Home page')

def About(request):
    return HttpResponse('About page')

def Contact(request):
    return HttpResponse('Contact page')