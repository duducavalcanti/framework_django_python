from django.urls import path
from .views import personagens

urlpatterns = [
    path('', personagens, name='personagens'),
]