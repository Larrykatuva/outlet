from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from src.serializers.authentication_serializers import RegisterUserSerializer, VerificationSerializer, \
    LoginUserSerializer, LoginResponseSerializer, ProfileSerializer, ProfileReadonlySerializer, ResetUserSerializer, \
    PasswordSerializer
from src.services.authentication.authentication_service import UserService
from src.services.authentication.profile_service import ProfileService
from rest_framework.permissions import IsAuthenticated


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    user_service = UserService()

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            self.user_service.register_user(data)
            return Response({"message": "User created successfully check verification code in your email."},
                            status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class VerificationAPIView(CreateAPIView):
    serializer_class = VerificationSerializer
    user_service = UserService()

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            code = serializer.validated_data.get('code')
            self.user_service.verify_user(code)
            return Response({"message": "Email verified successfully"}, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(CreateAPIView):
    serializer_class = LoginUserSerializer
    user_service = UserService()

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            res = self.user_service.login_user(username=data.get('username'), password=data.get('password'))
            self.serializer_class = LoginResponseSerializer
            serialized_data = self.serializer_class(res)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(CreateAPIView):
    serializer_class = ResetUserSerializer
    user_service = UserService()

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            code = self.user_service.reset_user(email=data.get('email'))
            return Response(
                {'message': 'Reset code sent successfully. Please check your email', 'code': code},
                status=status.HTTP_200_OK)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class SetPasswordAPIView(CreateAPIView):
    serializer_class = PasswordSerializer
    user_service = UserService()

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            self.user_service.set_new_password(code=data.get('code'), password=data.get('password'),
                                               confirm_password=data.get('confirm_password'))
            return Response({'message': 'Password updated successfully'},
                            status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(CreateAPIView):
    serializer_class = ProfileSerializer
    profile_service = ProfileService()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            image = request.FILES.get('image')
            data = serializer.data
            data['image'] = image
            profile = self.profile_service.create_profile(user=request.user, kwargs=data)
            self.serializer_class = ProfileReadonlySerializer
            serialized_data = self.serializer_class(profile)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(err.args[0], status=status.HTTP_400_BAD_REQUEST)


class AllProfilesAPIView(ListAPIView):
    serializer_class = ProfileReadonlySerializer
    profile_service = ProfileService()
    queryset = profile_service.get_all_profiles()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset


class UserProfileAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    profile_service = ProfileService()
    queryset = profile_service.get_all_profiles()
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.method == 'GET':
            self.serializer_class = ProfileReadonlySerializer
        if self.request.method == 'PATCH' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            profile_id = self.kwargs.get('id')
            self.profile_service.delete_user_profile_image(id=profile_id)
        self.serializer_class = ProfileReadonlySerializer
        return self.queryset.filter()
