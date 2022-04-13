from src.models import Outlet
from rest_framework import serializers
from src.serializers.authentication_serializers import ReadOnlyUserSerializer


class OutletSerializer(serializers.ModelSerializer):
    image = serializers.FileField(allow_empty_file=False)

    class Meta:
        model = Outlet
        fields = ['name', 'image', 'location', 'latitude', 'longitude']


class ReadOnlyOutletSerializer(serializers.ModelSerializer):
    user = ReadOnlyUserSerializer()

    class Meta:
        model = Outlet
        fields = ['id', 'name', 'image', 'location', 'latitude', 'longitude', 'created_at', 'updated_at', 'user']
