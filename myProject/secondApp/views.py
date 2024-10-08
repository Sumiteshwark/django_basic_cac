from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

from django.http import HttpResponse


# Create your views here.

def SecondAppHome(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'secondApp/index.html', {'chais': chais})

def ChaiDetail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'secondApp/chai_detail.html', {'chai': chai})