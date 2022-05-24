from src.models import Order, OrderItem, Cart
import uuid


class OrderItemService:

    @staticmethod
    def create_order_item(
            order: Order,
            cart: Cart
    ) -> OrderItem:
        return OrderItem.objects.create(
            order=order,
            price=cart.food.price,
            seller=cart.food.outlet.user.username,
            outlet=cart.food.outlet,
            food_name=cart.food.name,
            quantity=cart.quantity,
            food=cart.food
        )

    @staticmethod
    def get_order_by_id(id: uuid):
        try:
            return OrderItem.objects.get(pk=id)
        except OrderItem.DoesNotExist:
            return None
