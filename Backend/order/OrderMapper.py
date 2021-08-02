from app.apps.core.mapper import Mapper
from .OrderBO import OrderObject
from app.configs.base import db_connector


class OrderMapper(Mapper):

    def find_by_key(cnx: db_connector, key: int) -> OrderObject:
        """Gets an Order by the key 'id'."""
        result = None

        cursor = cnx.cursor(buffered=True)
        command = """
        SELECT
        id, quantity, annotation, tablenumber, product_id, order_status
        FROM person WHERE id=%s
        """
        cursor.execute(command, (key, ))
        entity = cursor.fetchone()

        try:
            (id, quantity, annotation, tablenumber, product_id, order_status) = entity
            result = OrderObject(
                id_=id,
                quantity=quantity,
                annotation=annotation,
                tablenumber=tablenumber,
                product_id=product_id,
                order_status=order_status,
            )
        except IndexError:
            result = None

        cnx.commit()
        cursor.close()

        return result

    def find_all(cnx: db_connector):
        """Gibt alle Order zurück"""

        result = []
        cursor = cnx.cursor()
        cursor.execute("""
        SELECT id, quantity,  annoation, tablenumber, 
                product_id, order_status, 
        FROM order
        """)
        tuples = cursor.fetchall()

        for (id, quantity, annotation, tablenumber, product_id, order_status) in tuples:
            order = OrderObject()
            order.id_ = id
            order.quantity = quantity
            order.annotation = annotation
            order.tablenumber = tablenumber
            order.product_id = product_id
            order.order_status = order_status


            result.append(order)

        cnx.commit()
        cursor.close()

        return result

    @staticmethod
    def insert(cnx: db_connector, object: OrderObject) -> OrderObject:
        """Creates Order Object."""
        cursor = cnx.cursor(buffered=True)
        command = """
            INSERT INTO order (
                 quantity, annotation, tablenumber,
                 product_id, order_status
            ) VALUES (%s,%s,%s,%s,%s)
        """
        cursor.execute(command, (
            object.quantity,
            object.annotation,
            object.tablenumber,
            object.product_id,
            object.order_status
        ))
        cnx.commit()
        cursor.execute("SELECT MAX(id) FROM order")
        max_id = cursor.fetchone()[0]
        object.id_ = max_id
        return object

    def update(cnx: db_connector, object: OrderObject):
        """Updates an Order."""
        cursor = cnx.cursor(buffered=True)
        command = """UPDATE order " + 
        "SET 
        quantity=%s, 
        annotation=%s, 
        tablenumber=%s, 
        product_id=%s, 
        order_status=%s
        WHERE id=%s"""
        cursor.execute(command, (
            object.quantity,
            object.annotation,
            object.tablenumber,
            object.product_id,
            object.order_status,
            object.id_
        ))

        cnx.commit()
        cursor.close()
