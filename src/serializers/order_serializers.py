from rest_framework import serializers
from src.models import Order, OrderItem
from src.serializers.cart_serializers import ReadOnlyFoodSerializer
from src.serializers.outlet_serializers import ReadOnlyOutletSerializer
from src.serializers.authentication_serializers import ReadOnlyUserSerializer


class ReadOnlyOrderItemSerializer(serializers.ModelSerializer):
    food = ReadOnlyFoodSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'price', 'seller', 'food_name', 'quantity', 'created_at', 'updated_at', 'food']


class ReadOnlyOrderSerializer(serializers.ModelSerializer):
    order_items = ReadOnlyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'amount', 'created_at', 'updated_at', 'order_items']


class OutletOrderSerializer(serializers.ModelSerializer):
    order_items = ReadOnlyOrderItemSerializer(many=True)
    user = ReadOnlyUserSerializer()

    class Meta:
        model = Order
        fields = ['id', 'amount', 'created_at', 'updated_at', 'user', 'order_items']
