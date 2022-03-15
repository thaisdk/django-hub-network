from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('projects.urls')),  # Main
    path('admin/', admin.site.urls),
    
]
