from django.contrib import admin
from django.urls import path, include
from outlet import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('src.urls.authentication_urls')),
    path('outlet/', include('src.urls.outlet_urls')),
    path('cart/', include('src.urls.cart_urls')),
    path('order/', include('src.urls.order_urls')),
    path('', include('outlet.swagger_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
