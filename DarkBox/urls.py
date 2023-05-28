from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('phones.urls')),
    path('users/', include('users.urls')),
    path('api/', include('api.urls', namespace='api'))
]
