from django.urls import path
from src.views.order_views import PlaceOrderAPIView, MyOrdersAPIView, OutletOrdersAPIView, OrderCallBack


urlpatterns = [
    path('place-order', PlaceOrderAPIView.as_view(), name='place-order'),
    path('user-orders', MyOrdersAPIView.as_view(), name='user-orders'),
    path('outlet-orders', OutletOrdersAPIView.as_view(), name='outlet-orders'),
    path('call-back', OrderCallBack.as_view(), name='call-back')
]
