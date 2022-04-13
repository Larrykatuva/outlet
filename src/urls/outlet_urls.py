from django.conf.urls.static import static
from django.urls import path
from src.views.outlet_views import CreateOutletAPIView, OutletsAPIView, OutletAPIView
from outlet import settings


urlpatterns = [
    path('create', CreateOutletAPIView.as_view(), name='create-outlet'),
    path('all', OutletsAPIView.as_view(), name="list-outlets"),
    path('outlet/<id>', OutletAPIView.as_view(), name="outlet"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)