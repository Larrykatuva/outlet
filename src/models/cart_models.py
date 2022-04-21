from django.db import models
from django.db.models.deletion import CASCADE
from src.models import User, Food
import uuid


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, to_field='id', on_delete=CASCADE)
    food = models.ForeignKey(Food, to_field='id', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Favourite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, to_field='id', on_delete=CASCADE)
    food = models.ForeignKey(Food, to_field='id', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

