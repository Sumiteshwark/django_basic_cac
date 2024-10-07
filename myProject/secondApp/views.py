from django.shortcuts import render

# Create your views here.

def SecondAppHome(request):
    return render(request, 'secondApp/index.html')
