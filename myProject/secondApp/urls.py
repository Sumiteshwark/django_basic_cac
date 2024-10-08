from django.urls import path
from . import views

urlpatterns = [
    path('', views.SecondAppHome, name='secondAppHome'),
    path('<int:chai_id>/', views.ChaiDetail, name='chai_detail'),
]
