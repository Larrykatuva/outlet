from src.models.authentication_models import User, Code, Profile
from rest_framework import serializers


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class RegisterResponseSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=256)

    class Meta:
        fields = ['message']


class VerificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Code
        fields = ['code']


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=256)
    password = serializers.CharField(max_length=256)

    class Meta:
        fields = ['username', 'password']


class ResetUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=256)

    class Meta:
        fields = ['email']


class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100)
    confirm_password = serializers.CharField(max_length=100)

    class Meta:
        model = Code
        fields = ['code', 'password', 'confirm_password']


class ReadOnlyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'is_verified', 'is_staff', 'is_superuser', 'created_at',
                  'updated_at']


class TokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=555)
    refresh_token = serializers.CharField(max_length=555)

    class Meta:
        fields = ['access_token', 'refresh_token']


class LoginResponseSerializer(serializers.Serializer):
    user = ReadOnlyUserSerializer()
    tokens = TokenSerializer()

    class Meta:
        fields = ['user', 'tokens']


class ProfileSerializer(serializers.ModelSerializer):
    image = serializers.FileField(allow_empty_file=False)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'gender', 'date_of_birth', 'image']


class ProfileReadonlySerializer(serializers.ModelSerializer):
    user = ReadOnlyUserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'phone', 'gender', 'date_of_birth', 'image', 'created_at',
                  'updated_at', 'user']

