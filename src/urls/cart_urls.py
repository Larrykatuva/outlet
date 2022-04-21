from django.urls import path
from src.views.cart_views import CartAPIView, CartsAPIView, FavouriteAPIView, FavouritesAPIView


urlpatterns = [
    path('cart-items', CartsAPIView.as_view(), name='cart-items'),
    path('cart-item/<id>', CartAPIView.as_view(), name='cart-item'),
    path('favourite-items', FavouritesAPIView.as_view(), name='favourite-items'),
    path('favourite-item/<id>', FavouriteAPIView.as_view(), name='favourite-item')
]
