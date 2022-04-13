from django.db import models
from django.db.models.deletion import CASCADE
from src.models import User
import uuid


class Outlet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, to_field='id', on_delete=CASCADE)
    name = models.CharField(max_length=256, null=False)
    image = models.ImageField(upload_to='logo/', null=False)
    location = models.CharField(max_length=256, null=False)
    longitude = models.CharField(max_length=20, null=False)
    latitude = models.CharField(max_length=20, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

