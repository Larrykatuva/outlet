from django.db.models.query import Q, QuerySet
from src.models import Outlet
import uuid


class OutletService:

    @staticmethod
    def create_outlet(kwargs: dict) -> Outlet:
        return Outlet.objects.create(**kwargs)

    @staticmethod
    def get_all_outlets() -> QuerySet[Outlet]:
        return Outlet.objects.all()

    @staticmethod
    def get_user_outlet(user_id: uuid) -> Outlet:
        try:
            return Outlet.objects.get(user=user_id)
        except Outlet.DoesNotExist:
            return None

    @staticmethod
    def delete_outlet_logo(id: uuid) -> None:
        try:
            Outlet.objects.get(id=id).image.delete(save=True)
        except Outlet.DoesNotExist:
            pass
