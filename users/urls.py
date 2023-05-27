from django.urls import path
from .views import lol

urlpatterns = [
    path('', lol, name='users'),
]
