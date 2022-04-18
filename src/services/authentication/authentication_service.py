from src.models.authentication_models import User, Code
from src.utils.email_utils import Email
from datetime import datetime, timedelta, date
from src.errors.authentication.user_errors import UserErrors
from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken
import string
import random
import pytz


class UserService:

    def __init__(self):
        self.user_errors = UserErrors()
        self.utc = pytz.UTC

    @staticmethod
    def generate_random_code() -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

    @staticmethod
    def calculate_expiry_time() -> datetime:
        """Calculating expiry time for verification code"""
        updated_time = datetime.now() + timedelta(hours=24)
        return updated_time

    def create_verification_code(self, user: User, code: str) -> Code:
        expiry = self.calculate_expiry_time()
        return Code.objects.create(user=user, code=code, expiry=expiry)

    def send_verification_email(self, email_subject: str, email_body: str, user: User) -> str:
        activate_code = self.generate_random_code()
        self.create_verification_code(user, activate_code)
        email_body = email_body + activate_code
        Email.send(email_subject, email_body, [user.email])
        return activate_code

    def register_user(self, kwargs) -> User:
        user = User.objects.create_user(**kwargs)
        email_subject = 'Activate your Account'
        email_body = 'Your activation code is '
        self.send_verification_email(email_subject, email_body, user)
        return user

    def verify_user(self, code: str) -> int:
        current_time = datetime.now()
        code = Code.objects.filter(code=code).order_by('-id')[:1]
        if len(code) < 1:
            raise Exception(self.user_errors.raise_invalid_code())
        if User.objects.filter(id=code[0].user.id)[0].is_verified:
            raise Exception(self.user_errors.raise_code_used())
        # if code[0].expiry < current_time:
        #     raise Exception(self.user_errors.raise_verification_code_expired())
        return User.objects.filter(id=code[0].user.id).update(is_verified=True)

    def login_user(self, username: str, password: str) -> dict:
        try:
            user_auth = User.objects.get(username=username)
            if not user_auth.is_verified:
                raise Exception(self.user_errors.raise_email_not_verified())
            if not user_auth.is_active:
                raise Exception(self.user_errors.raise_account_inactive())
            user = auth.authenticate(email=user_auth.email, password=password)
            if not user:
                raise Exception(self.user_errors.raise_login_failed())
            tokens = RefreshToken.for_user(user)
            kwargs = {'user': user, 'tokens': {
                'refresh_token': str(tokens),
                'access_token': str(tokens.access_token)
            }}
            return kwargs
        except User.DoesNotExist:
            raise Exception(self.user_errors.raise_invalid_username())

    def reset_user(self, email: str) -> str:
        try:
            user = User.objects.get(email=email)
            email_subject = 'Reset your password'
            email_body = 'Your account reset code is '
            code = self.send_verification_email(email_subject, email_body, user)
            return code
        except User.DoesNotExist:
            raise Exception(self.user_errors.raise_invalid_email())

    def set_new_password(self, code: str, password, confirm_password) -> None:
        current_time = datetime.now()
        code = Code.objects.filter(code=code).order_by('-id')[:1]
        if len(code) < 1:
            raise Exception(self.user_errors.raise_invalid_code())
        # if code[0].expiry < current_time:
        #     raise Exception(self.user_errors.raise_verification_code_expired())
        if password != confirm_password:
            raise Exception(self.user_errors.raise_password_do_not_match())
        user = User.objects.filter(id=code[0].user.id)[0]
        user.set_password(password)
        user.save()


