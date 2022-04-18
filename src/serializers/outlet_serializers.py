from src.models import Outlet, Food, Comment, Star
from rest_framework import serializers
from src.serializers.authentication_serializers import ReadOnlyUserSerializer


class OutletSerializer(serializers.ModelSerializer):
    image = serializers.FileField(allow_empty_file=False)

    class Meta:
        model = Outlet
        fields = ['name', 'image', 'location', 'latitude', 'longitude']


class OutletDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = ['id', 'name', 'image', 'location', 'latitude', 'longitude', 'created_at', 'updated_at']


class ReadOnlyOutletSerializer(serializers.ModelSerializer):
    user = ReadOnlyUserSerializer()

    class Meta:
        model = Outlet
        fields = ['id', 'name', 'image', 'location', 'latitude', 'longitude', 'created_at', 'updated_at', 'user']


class FoodSerializer(serializers.ModelSerializer):
    CATEGORY = (
        ('STREETWISE', 'STREETWISE'),
        ('SNACKS', 'SNACKS'),
        ('CHICKEN DEALS', 'CHICKEN DEALS'),
        ('DRINKS', 'DRINKS'),
        ('HEAVY TAKE', 'HEAVY TAKE'),
        ('BREAKFAST', 'BREAKFAST'),
        ('LUNCH', 'LUNCH')
    )
    image = serializers.ImageField(allow_empty_file=False)
    category = serializers.ChoiceField(choices=CATEGORY)

    class Meta:
        model = Food
        fields = ['name', 'description', 'category', 'image', 'price']


class ReadOnlyFoodSerializer(serializers.ModelSerializer):
    outlet = OutletDetailsSerializer()

    class Meta:
        model = Food
        fields = ['id', 'name', 'description', 'image', 'category', 'price', 'likes', 'rating', 'created_at',
                  'updated_at', 'outlet']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['description', 'food']


class UpdateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['description']


class ReadOnlyCommentSerializer(serializers.ModelSerializer):
    food = ReadOnlyFoodSerializer()
    user = ReadOnlyUserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'description', 'created_at', 'updated_at', 'user', 'food']


class StarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Star
        fields = ['value', 'food']

    def validate(self, attrs):
        value = attrs.get('value')

        if value < 1 or value > 5:
            raise Exception({"value": ['value should not be less than 0 or greater than 5']})

        return attrs


class ReadOnlyStarSerializer(serializers.ModelSerializer):
    food = ReadOnlyFoodSerializer()
    user = ReadOnlyUserSerializer()

    class Meta:
        model = Star
        fields = ['id', 'value', 'created_at', 'updated_at', 'user', 'food']
