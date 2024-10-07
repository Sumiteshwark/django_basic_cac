from django.urls import path
from . import views

urlpatterns = [
    path('', views.SecondAppHome, name='secondAppHome'),
]
