from django.shortcuts import render
from .models import ChaiVariety

# Create your views here.

def SecondAppHome(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'secondApp/index.html', {'chais': chais})
