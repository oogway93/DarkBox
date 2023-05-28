from django.urls import include, path
from rest_framework import routers

from api.views import PhonesModelViewSet

app_name = 'api'
router = routers.SimpleRouter()
router.register(r'phones', PhonesModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
