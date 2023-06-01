from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('phones', include('phones.urls')),
                  path('users/', include('users.urls')),
                  path('laptops', include('laptops.urls')),
                  path('api/', include('api.urls', namespace='api')),
                  path('', include('manufactures.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
