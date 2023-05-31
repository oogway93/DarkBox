from django.urls import path
from .views import CatalogLaptop

urlpatterns = [
    path('', CatalogLaptop, name='laptop')
]

