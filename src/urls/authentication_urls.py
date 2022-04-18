from django.conf.urls.static import static
from django.urls import path
from src.views.authentication_views import RegisterAPIView, VerificationAPIView, LoginAPIView, ProfileAPIView, \
    UserProfileAPIView, AllProfilesAPIView, ResetPasswordAPIView, SetPasswordAPIView
from outlet import settings


urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('verify-email', VerificationAPIView.as_view(), name="verify-email"),
    path('request-reset-code', ResetPasswordAPIView.as_view(), name="request-code"),
    path('set-new-password', SetPasswordAPIView.as_view(), name='set-new-password'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('profile', ProfileAPIView.as_view(), name='profile'),
    path('profiles', AllProfilesAPIView.as_view(), name='profiles'),
    path('profile/<id>', UserProfileAPIView.as_view(), name='user-profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
