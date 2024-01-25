from django.urls import path, include 
from .views import *

urlpatterns = [
    path('', Home, name='home-page'),
    path('services', Services, name='services'),
    path('dashboard', conview, name='dashboard'),
    path('services1', Services1, name='services1'),
    path('services2', Services2, name='services2'),
    path('services3', Services3, name='services3'),
    path('services4', Services4, name='services4'),
    path('', include('django_dyn_dt.urls')),
]

