from django.urls import path
from .views import CatalogPhone

urlpatterns = [
    path('', CatalogPhone, name='phone')
]

