from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bhanuistheonlyadmin/', admin.site.urls),  # Admin Panel
    path('', include('myapp.urls')),  # Includes all app URLs
]
