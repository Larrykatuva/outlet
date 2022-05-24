from src.models import Order, User
from django.db.models.query import QuerySet
import uuid


class OrderService:

    @staticmethod
    def create_order(
            user: User,
            amount: float
    ) -> Order:
        return Order.objects.create(
            user=user,
            amount=amount
        )

    @staticmethod
    def get_order_by_id(id: uuid) -> Order:
        try:
            return Order.objects.get(pk=id)
        except Order.DoesNotExist:
            return None

    @staticmethod
    def get_user_orders(user: User) -> QuerySet[Order]:
        return Order.objects.filter(
            user=user
        ).prefetch_related('order_items')

    @staticmethod
    def get_outlet_orders(user: User) -> QuerySet[Order]:
        return Order.objects.filter(
            order_items__outlet__user=user
        ).prefetch_related('order_items')
