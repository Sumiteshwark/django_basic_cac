from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
#     return HttpResponse('Home page')
    return render(request, 'index.html')

def About(request):
    return HttpResponse('About page')

def Contact(request):
    return HttpResponse('Contact page')