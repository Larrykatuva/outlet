from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('src.urls.authentication_urls')),
    path('outlet/', include('src.urls.outlet_urls')),
    path('', include('outlet.swagger_urls')),
]
