from .OrderMapper import OrderMapper
from .OrderBO import OrderObject
from Backend.configs.base import db_connector


class OrderAdministration:
    """Order Manager class. For managing database interactions."""

    @staticmethod
    def create_order(quantity: int, annotation: str, table_: int, 
                    product: int, ) -> OrderObject:
        """Create an OrderObject."""
        with db_connector as db:
            cnx = db._cnx
            order = OrderObject
            order.quantity=quantity
            order.annotation=annotation
            order.table_=table_
            order.product=product
            return OrderMapper.insert(cnx=cnx, object=order)

    @staticmethod
    def get_all_orders():
        """Returns all Orders"""
        with db_connector as db:
            cnx = db._cnx
            return OrderMapper.find_all(cnx=cnx)

    @staticmethod
    def get_order_by_id(id_: int) -> OrderObject:
        """Returns Orders by id."""
        with db_connector as db:
            cnx = db._cnx
            return OrderMapper.find_by_key(cnx=cnx, key=id_)

    @staticmethod
    def send_order(order: OrderObject):
        """Sends an Order"""
        with db_connector as db:
            cnx = db._cnx
            OrderMapper.update(cnx=cnx, order=order)

    @staticmethod
    def update_order(order: OrderObject):
        with db_connector as db:
            cnx=db._cnx
            OrderMapper.update(cnx=cnx, order=order)

    @staticmethod
    def delete_order(id_: int):
        """Deletes an Order"""
        with db_connector as db:
            cnx = db._cnx
            OrderMapper.delete(cnx=cnx, id_=id_)