from src.models import Outlet
from collections.abc import Iterable
import uuid


class OutletService:

    @staticmethod
    def create_outlet(kwargs: dict) -> Outlet:
        return Outlet.objects.create(**kwargs)

    @staticmethod
    def get_all_outlets() -> Iterable[Outlet]:
        return Outlet.objects.all()

    @staticmethod
    def delete_outlet_logo(id: uuid):
        try:
            Outlet.objects.get(id=id).image.delete(save=True)
        except Outlet.DoesNotExist:
            pass
