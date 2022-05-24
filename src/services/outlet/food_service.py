from src.models import Food, Star, User, Comment
from django.db.models.query import Q, QuerySet
import uuid


class FoodService:

    @staticmethod
    def create_food(kwargs: dict) -> Food:
        return Food.objects.create(
            likes=0,
            rating=0,
            **kwargs
        )

    @staticmethod
    def get_all_foods() -> QuerySet[Food]:
        return Food.objects.all().prefetch_related('outlet')

    @staticmethod
    def add_food_rating(
            user: User,
            value: int,
            food: uuid
    ) -> Star:
        current_star = Star.objects.filter(food=food).count()
        rate_value = value
        if current_star > 0:
            food = Food.objects.get(id=food)
            stars = Star.objects.filter(food=food.id)
            total_rating = rate_value
            for star in stars:
                total_rating = total_rating + star.value
            rate_value = round(total_rating / (current_star + 1))
            food = food.id
        Food.objects.filter(id=food).update(rating=rate_value)
        user = User.objects.get(id=user)
        food = Food.objects.get(id=food)
        return Star.objects.create(
            user=user,
            food=food,
            value=value
        )

    @staticmethod
    def create_food_comment(
            user: User,
            desc: str,
            food: Food
    ) -> Comment:
        food = Food.objects.get(id=food)
        return Comment.objects.create(
            user=user,
            description=desc,
            food=food
        )

    @staticmethod
    def get_food_ratings(food: Food) -> QuerySet[Food]:
        return Star.objects.filter(food=food)

    @staticmethod
    def get_food_comments(food: uuid) -> QuerySet[Comment]:
        return Comment.objects.filter(food=food)

    @staticmethod
    def get_all_comments() -> QuerySet[Comment]:
        return Comment.objects.all()

    @staticmethod
    def delete_food_image(id: uuid) -> None:
        try:
            Food.objects.get(id=id).image.delete(save=True)
        except Food.DoesNotExist:
            pass

    @staticmethod
    def get_food_by_id(id):
        try:
            return Food.objects.get(pk=id)
        except Food.DoesNotExist:
            return None

