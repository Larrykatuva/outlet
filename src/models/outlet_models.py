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


class Food(models.Model):
    CATEGORY = (
        ('STREETWISE', 'STREETWISE'),
        ('SNACKS', 'SNACKS'),
        ('CHICKEN DEALS', 'CHICKEN DEALS'),
        ('DRINKS', 'DRINKS'),
        ('HEAVY TAKE', 'HEAVY TAKE'),
        ('BREAKFAST', 'BREAKFAST'),
        ('LUNCH', 'LUNCH')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY, max_length=256)
    image = models.ImageField(upload_to='food/', null=False)
    price = models.FloatField()
    likes = models.IntegerField()
    rating = models.IntegerField()
    outlet = models.ForeignKey(Outlet, to_field='id', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, to_field='id', on_delete=CASCADE)
    food = models.ForeignKey(Food, to_field='id', on_delete=CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Star(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, to_field='id', on_delete=CASCADE)
    food = models.ForeignKey(Food, to_field='id', on_delete=CASCADE)
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
