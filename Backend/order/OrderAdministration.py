from .OrderMapper import OrderMapper
from .OrderBO import OrderObject
from app.configs.base import db_connector


class OrderAdministration:
    """Order Manager class. For managing database interactions."""

    @staticmethod
    def create_order(quantity: int, annotation: str, tablenumber: int, product_id: int, 
                    order_status: bool) -> OrderObject:
        """Create an OrderObject."""
        with db_connector as db:
            cnx = db._cnx
            order = OrderObject
            order.quantity=quantity
            order.annotation=annotation
            order.tablenumber=tablenumber
            order.product_id=product_id
            order.order_status=order_status
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