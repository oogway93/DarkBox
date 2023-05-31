from django.urls import path

from manufactures.views import Base

urlpatterns = [
    path('', Base)
]
