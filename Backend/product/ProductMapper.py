from Backend.core.mapper import Mapper
from .ProductBO import ProductObject
from Backend.configs.base import db_connector
from Backend.profile.ProfileAdministration import ProfileAdministration


class ProductMapper(Mapper):

    def find_by_name(cnx: db_connector, name: str) -> ProductObject:
        """Gets a product by the name."""
        result = None

        cursor = cnx.cursor(buffered=True)
        command = """
        SELECT id, price, name, description from `mydb`.`product`
        WHERE name=%s
        """
        cursor.execute(command, (name, ))
        entity = cursor.fetchone()

        try:
            (id, name, price, description) = entity
            result = ProductObject(
                id_=id,
                name=name,
                price=price,
                description=description
            )
        except TypeError:
            result = None

        cnx.commit()
        cursor.close()

        return result

    def find_by_key(cnx: db_connector, key: int) -> ProductObject:
        """Gets a Product by the key 'id'."""
        result = None

        cursor = cnx.cursor(buffered=True)
        command = """
        SELECT
        id, name, price, description
        FROM product WHERE id=%s
        """
        cursor.execute(command, (key, ))
        entity = cursor.fetchone()

        try:
            (id, name, price, description) = entity
            result = ProductObject(
                id_=id,
                name=name,
                price=price,
                description=description
            )
        except IndexError:
            result = None

        cnx.commit()
        cursor.close()

        return result

    @staticmethod
    def insert(cnx: db_connector, object: ProductObject) -> ProductObject:
        """Creates Product Object."""
        cursor = cnx.cursor(buffered=True)
        command = """
            INSERT INTO product (
                 name, price, descritopion
            ) VALUES (%s,%s)
        """
        cursor.execute(command, (
            object.name,
            object.price,
            object.description
        ))
        cnx.commit()
        cursor.execute("SELECT MAX(id) FROM product")
        max_id = cursor.fetchone()[0]
        object.id_ = max_id
        ProfileAdministration.insert_profile(profile=None, product=object)
        return object

    def update(cnx: db_connector, product: ProductObject):
        """Updates a Product."""
        cursor = cnx.cursor(buffered=True)
        command = "UPDATE product " + "SET name=%s, price=%s, description=%s WHERE id=%s"
        cursor.execute(command, (
            product.name,
            product.price,
            product.description
        ))

        cnx.commit()
        cursor.close()

    def delete(cnx: db_connector, product: int):
        """Deletes a Product."""
        cursor = cnx.cursor(buffered=True)
        command = ("DELETE FROM product WHERE id=%s")
        try:
            cursor.execute(command, (product,))
        except Exception:
            print("Product does not exist!")

        cnx.commit()
        cursor.close()
