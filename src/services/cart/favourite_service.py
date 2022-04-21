from src.models import Favourite, Food, User
from django.db.models.query import QuerySet


class FavouriteService:

    @staticmethod
    def add_to_favourite(user: User, food: Food) -> QuerySet[Favourite]:
        return Favourite.objects.create(food=food, user=user)

    @staticmethod
    def get_all_favourite_items() -> QuerySet[Favourite]:
        return Favourite.objects.all()

    @staticmethod
    def get_user_favourites(user: User) -> QuerySet[Favourite]:
        return Favourite.objects.filter(user=user)
    