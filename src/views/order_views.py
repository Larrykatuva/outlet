from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from src.services.order.order_service import OrderService
from src.services.order.order_item_service import OrderItemService
from src.services.cart.cart_service import CartService
from src.serializers.order_serializers import ReadOnlyOrderSerializer, OutletOrderSerializer
from src.services.order.mpesa_service import MpesaService
from src.services.authentication.profile_service import ProfileService


class PlaceOrderAPIView(CreateAPIView):
    order_service = OrderService()
    order_item_service = OrderItemService()
    cart_service = CartService()
    mpesa_service = MpesaService()
    profile_service = ProfileService

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            cart_foods = self.cart_service.get_user_cart_items(user=user)
            if cart_foods.count() > 0:
                order_amount = self.cart_service.calculate_total_amount(cart_foods=cart_foods)
                order = self.order_service.create_order(user=user, amount=order_amount)
                for cart_food in cart_foods:
                    self.order_item_service.create_order_item(order=order, cart=cart_food)
                self.cart_service.delete_cart_items(user=user)
                profile = self.profile_service.get_user_profile(user=request.user)
                payment = self.mpesa_service.initiate_transaction(amount=order.amount, phone="254720460519",
                                                                  transaction_desc="pay order", order=order)
                print(payment)
                return Response({"message": ['Order placed successfully']},
                                status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": ['Your cart is empty add foods and try again']},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class MyOrdersAPIView(ListAPIView):
    serializer_class = ReadOnlyOrderSerializer
    order_service = OrderService()

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.order_service.get_user_orders(user=self.request.user)
        return queryset


class OutletOrdersAPIView(ListAPIView):
    serializer_class = OutletOrderSerializer
    order_service = OrderService()

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.order_service.get_outlet_orders(user=self.request.user)
        return queryset


class OrderCallBack(CreateAPIView):

    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response({"message": ['Your cart is empty add foods and try again']},
                        status=status.HTTP_200_OK)

