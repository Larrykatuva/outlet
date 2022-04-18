from src.models import Profile, User
from src.errors.authentication.profile_errors import ProfileErrors
from django.db.models.query import Q, QuerySet
import uuid


class ProfileService:

    def __init__(self):
        self.profile_errors = ProfileErrors()

    def create_profile(self, user: User, kwargs: dict) -> Profile:
        if Profile.objects.filter(user=user).exists():
            raise Exception(self.profile_errors.raise_profile_exists())
        return Profile.objects.create(user=user, **kwargs)

    @staticmethod
    def update_profile(id: uuid, kwargs: dict) -> int:
        return Profile.objects.filter(pk=id).update(**kwargs)

    @staticmethod
    def get_all_profiles() -> QuerySet[Profile]:
        return Profile.objects.all().prefetch_related('user')

    @staticmethod
    def delete_user_profile_image(id: uuid):
        try:
            Profile.objects.get(id=id).image.delete(save=True)
        except Profile.DoesNotExist:
            pass

