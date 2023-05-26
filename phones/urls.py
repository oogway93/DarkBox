from django.urls import path
from .views import AvailableCatalog

urlpatterns = [
    path('', AvailableCatalog),
]

