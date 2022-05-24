from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from src.models import User, Food, Outlet
import uuid


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, to_field='id', on_delete=DO_NOTHING)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, to_field='id', on_delete=CASCADE, related_name='order_items')
    price = models.FloatField()
    seller = models.CharField(max_length=256)
    outlet = models.ForeignKey(Outlet, to_field='id', on_delete=DO_NOTHING)
    food_name = models.CharField(max_length=256)
    quantity = models.IntegerField()
    food = models.ForeignKey(Food, to_field='id', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
