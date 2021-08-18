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
        id, quantity, annotation, table_, product
        FROM person WHERE id=%s
        """
        cursor.execute(command, (key, ))
        entity = cursor.fetchone()

        try:
            (id, quantity, annotation, table_, product) = entity
            result = OrderObject(
                id_=id,
                quantity=quantity,
                annotation=annotation,
                table_=table_,
                product=product,
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
        SELECT id, quantity,  annoation, table_, 
                product, 
        FROM order
        """)
        tuples = cursor.fetchall()

        for (id, quantity, annotation, table_, product) in tuples:
            order = OrderObject()
            order.id_ = id
            order.quantity = quantity
            order.annotation = annotation
            order.table_ = table_
            order.product = product


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
                 quantity, annotation, table_,
                 product
            ) VALUES (%s,%s,%s,%s)
        """
        cursor.execute(command, (
            object.quantity,
            object.annotation,
            object.table_,
            object.product,
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
        table_=%s, 
        product=%s, 
        WHERE id=%s"""
        cursor.execute(command, (
            object.quantity,
            object.annotation,
            object.table_,
            object.product,
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