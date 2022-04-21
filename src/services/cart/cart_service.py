from src.models import Cart, Food, User
from django.db.models.query import QuerySet


class CartService:

    @staticmethod
    def add_to_cart(food: Food, user: User) -> Cart:
        return Cart.objects.create(user=user, food=food)

    @staticmethod
    def get_all_cart_foods() -> QuerySet[Cart]:
        return Cart.objects.all()

    @staticmethod
    def get_user_cart_items(user: User) -> QuerySet[Cart]:
        return Cart.objects.filter(user=user)


