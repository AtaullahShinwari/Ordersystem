from Backend.core.mapper import Mapper
from .OrderBO import OrderObject
from Backend.configs.base import db_connector


class OrderMapper(Mapper):

    def find_by_key(cnx: db_connector, key: int) -> OrderObject:
        """Gets an Order by the key 'id'."""
        result = None

        cursor = cnx.cursor(buffered=True)
        command = """
        SELECT
        id, quantity, annotation, tablenumber, product_id
        FROM person WHERE id=%s
        """
        cursor.execute(command, (key, ))
        entity = cursor.fetchone()

        try:
            (id, quantity, annotation, tablenumber, product_id) = entity
            result = OrderObject(
                id_=id,
                quantity=quantity,
                annotation=annotation,
                tablenumber=tablenumber,
                product_id=product_id,
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
                product_id, 
        FROM order
        """)
        tuples = cursor.fetchall()

        for (id, quantity, annotation, tablenumber, product_id) in tuples:
            order = OrderObject()
            order.id_ = id
            order.quantity = quantity
            order.annotation = annotation
            order.tablenumber = tablenumber
            order.product_id = product_id


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
                 product_id
            ) VALUES (%s,%s,%s,%s)
        """
        cursor.execute(command, (
            object.quantity,
            object.annotation,
            object.tablenumber,
            object.product_id,
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
        WHERE id=%s"""
        cursor.execute(command, (
            object.quantity,
            object.annotation,
            object.tablenumber,
            object.product_id,
            object.id_
        ))

        cnx.commit()
        cursor.close()

    def delete(cnx: db_connector, order: int):
        """Deletes an order."""
        cursor = cnx.cursor(buffered=True)
        command = ("DELETE FROM order WHERE id=%s")
        try:
            cursor.execute(command, (order,))
        except:
            print("Order does not exist!")

        cnx.commit()
        cursor.close()