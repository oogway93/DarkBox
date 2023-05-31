from django.urls import path
from .views import AvailableCatalog, Base

urlpatterns = [
    path('', AvailableCatalog, name='home')
]

