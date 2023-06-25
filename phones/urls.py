from django.urls import path
from .views import CatalogPhone, Base

urlpatterns = [
    path('phones', CatalogPhone, name='phone'),
    path('', Base, name='home')
]
