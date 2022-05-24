from src.serializers.outlet_serializers import ReadOnlyFoodSerializer
from src.serializers.authentication_serializers import ReadOnlyUserSerializer
from src.models import Cart, Favourite
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    quantity = serializers.FloatField(required=True, min_value=1)

    class Meta:
        model = Cart
        fields = ['food', 'quantity']


class UpdateCartSerializer(serializers.ModelSerializer):
    quantity = serializers.FloatField(required=True, min_value=1)

    class Meta:
        model = Cart
        fields = ['quantity']


class ReadOnlyCartSerializer(serializers.ModelSerializer):
    user = ReadOnlyUserSerializer()
    food = ReadOnlyFoodSerializer()

    class Meta:
        model = Cart
        fields = ['id', 'quantity', 'created_at', 'updated_at', 'user', 'food']


class FavouriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourite
        fields = ['food']


class ReadOnlyFavouriteSerializer(serializers.ModelSerializer):
    user = ReadOnlyUserSerializer()
    food = ReadOnlyFoodSerializer()

    class Meta:
        model = Favourite
        fields = ['id', 'created_at', 'updated_at', 'user', 'food']

