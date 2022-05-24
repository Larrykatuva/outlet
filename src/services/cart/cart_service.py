from src.models import Cart, Food, User
from django.db.models.query import QuerySet


class CartService:

    @staticmethod
    def add_to_cart(
            food: Food,
            user: User,
            quantity: int
    ) -> Cart:
        return Cart.objects.create(
            user=user,
            food=food,
            quantity=quantity
        )

    @staticmethod
    def check_cart_by_food(
            food: Food,
            user: User
    ) -> QuerySet[Cart]:
        return Cart.objects.filter(
            food=food,
            user=user
        )

    @staticmethod
    def update_food_quantity(
            food: Food,
            user: User,
            quantity: int
    ) -> Cart:
        current_quantity = Cart.objects.filter(
            food=food,
            user=user
        )[0].quantity
        print(current_quantity)
        new_quantity = current_quantity + quantity
        Cart.objects.filter(
            food=food
        ).update(quantity=new_quantity)
        return Cart.objects.get(food=food)

    @staticmethod
    def get_all_cart_foods() -> QuerySet[Cart]:
        return Cart.objects.all()

    @staticmethod
    def get_user_cart_items(user: User) -> QuerySet[Cart]:
        return Cart.objects.filter(user=user)

    @staticmethod
    def calculate_total_amount(cart_foods: QuerySet[Cart]) -> float:
        total_amount = 0
        for cart_food in cart_foods:
            food_amount = cart_food.food.price * cart_food.quantity
            total_amount += food_amount
        return total_amount

    @staticmethod
    def delete_cart_items(user: User) -> None:
        return Cart.objects.filter(user=user).delete()
