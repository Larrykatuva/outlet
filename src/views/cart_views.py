from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from src.serializers.cart_serializers import CartSerializer, ReadOnlyCartSerializer, FavouriteSerializer, \
    ReadOnlyFavouriteSerializer, UpdateCartSerializer
from src.services.cart.cart_service import CartService
from src.services.cart.favourite_service import FavouriteService
from src.services.outlet.food_service import FoodService


class CartsAPIView(ListCreateAPIView):
    serializer_class = CartSerializer
    cart_service = CartService()
    food_service = FoodService()

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            food = self.food_service.get_food_by_id(id=data.get('food'))
            food_in_cart = self.cart_service.check_cart_by_food(food=food, user=request.user)
            if food_in_cart.count() > 0:
                cart = self.cart_service.update_food_quantity(food=food, user=request.user,
                                                              quantity=data.get('quantity'))
            else:
                cart = self.cart_service.add_to_cart(food=food, user=request.user, quantity=data.get('quantity'))
            self.serializer_class = ReadOnlyCartSerializer
            serialized_data = self.serializer_class(cart)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        self.serializer_class = ReadOnlyCartSerializer
        queryset = self.cart_service.get_user_cart_items(user=self.request.user)
        return queryset


class CartAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateCartSerializer
    cart_service = CartService()
    queryset = cart_service.get_all_cart_foods()
    lookup_field = 'id'

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        self.serializer_class = ReadOnlyCartSerializer
        return self.queryset.filter()


class FavouritesAPIView(ListCreateAPIView):
    serializer_class = FavouriteSerializer
    favourite_service = FavouriteService()
    food_service = FoodService()

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            food = self.food_service.get_food_by_id(id=data.get('food'))
            favourite = self.favourite_service.add_to_favourite(user=request.user, food=food)
            self.serializer_class = ReadOnlyFavouriteSerializer
            serialized_data = self.serializer_class(favourite)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        self.serializer_class = ReadOnlyFavouriteSerializer
        queryset = self.favourite_service.get_user_favourites(user=self.request.user)
        return queryset


class FavouriteAPIView(RetrieveDestroyAPIView):
    serializer_class = ReadOnlyFavouriteSerializer
    favourite_service = FavouriteService()
    queryset = favourite_service.get_all_favourite_items()
    lookup_field = 'id'

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter()



