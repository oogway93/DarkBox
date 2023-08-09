from django.urls import include, path
from rest_framework import routers

from api.views import PhonesModelViewSet, LaptopsModelViewSet

app_name = 'api'
router = routers.SimpleRouter()
router.register(r'phones', PhonesModelViewSet)
router.register(r'laptops', LaptopsModelViewSet)

urlpatterns = [
    path('', include(router.urls), name='api')
]
urlpatterns += router.urls
