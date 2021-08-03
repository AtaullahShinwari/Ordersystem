from .OrderMapper import OrderMapper
from .OrderBO import OrderObject
from Backend.configs.base import db_connector


class OrderAdministration:
    """Profile Manager class. For managing database interactions."""

    @staticmethod
    def insert_Order(email: str, google_user_id: str) -> OrderObject:
        """Create a OrderObject."""
        with db_connector as db:
            cnx = db._cnx
            Order = OrderObject
            Order.email=email
            Order.google_user_id=google_user_id
            return OrderMapper.insert(cnx=cnx, object=Order)

    @staticmethod
    def get_Order_by_id(Order: int) -> OrderObject:
        """Returns Orders by id."""
        with db_connector as db:
            cnx = db._cnx
            return OrderMapper.find_by_key(cnx=cnx, key=Order)