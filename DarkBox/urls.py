from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('/phones', include('phones.urls')),
    path('users/', include('users.urls')),
    path('/laptops', include('laptops.urls')),
    path('api/', include('api.urls', namespace='api')),
    path('', include('manufactures.urls'))
]
