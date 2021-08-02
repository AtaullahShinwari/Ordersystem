from .ProductMapper import ProductMapper
from .ProductBO import ProductObject
from Backend.configs.base import db_connector


class ProductAdministration:
    """Profile Manager class. For managing database interactions."""

    @staticmethod
    def insert_product(name: str, price: float, description: str, menu_id:int) -> ProductObject:
        """Create a ProductObject."""
        with db_connector as db:
            cnx = db._cnx
            product = ProductObject
            product.name=name
            product.price=price
            product.description= description
            product.menu_id= menu_id
            return ProductMapper.insert(cnx=cnx, object=product)

    @staticmethod
    def get_product_by_id(product: int) -> ProductObject:
        """Returns Products by id."""
        with db_connector as db:
            cnx = db._cnx
            return ProductMapper.find_by_key(cnx=cnx, key=product)

    @staticmethod
    def get_product_by_name(name: str) -> ProductObject:
        """Returns products by name."""
        with db_connector as db:
            cnx = db._cnx
            return ProductMapper.find_by_name(cnx=cnx, name=name)

    @staticmethod
    def save_product(product: ProductObject):
        """Saves a Product"""
        with db_connector as db:
            cnx = db._cnx
            ProductMapper.update(cnx=cnx, product=product)

    @staticmethod
    def delete_product(product: int):
        """Deletes a Product"""
        with db_connector as db:
            cnx = db._cnx
            ProductMapper.delete(cnx=cnx, product=product)
