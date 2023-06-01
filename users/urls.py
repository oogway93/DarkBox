from django.urls import path, include

from users.views import Register, profile

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('profile/', profile, name='profile'),
]
