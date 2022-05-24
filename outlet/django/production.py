from outlet.django.base import *
import environ

env = environ.Env()
environ.Env.read_env()


DEBUG = env.bool('DJANGO_DEBUG', default=False)

SECRET_KEY = env.get_value('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST', default=[])

SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=True)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "SECURE_CONTENT_TYPE_NOSNIFF", default=True
)
