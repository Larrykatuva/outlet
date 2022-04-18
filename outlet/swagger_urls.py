from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path
from drf_yasg.generators import OpenAPISchemaGenerator
from outlet.settings import (
    MODE
)


class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, *args, **kwargs):
        schema = super().get_schema(*args, **kwargs)
        schema.basePath = '/sms-api/'
        return schema


if MODE == 'DEV':
    GENERATOR_CLASS = None
if MODE == 'SANDBOX':
    GENERATOR_CLASS = CustomOpenAPISchemaGenerator
if MODE == 'PRODUCTION':
    GENERATOR_CLASS = None

schema_view = get_schema_view(
    info=openapi.Info(
        title="OUTLET APP BACKEND APIs",
        default_version='v1',
        description="APIs made to be integrated with Outlet food ordering app",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="larry.katuva@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=GENERATOR_CLASS,
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]
