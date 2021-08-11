from .UpperCatMapper import UpperCatMapper
from .UpperCatBO import UpperCatObject
from Backend.configs.base import db_connector


class UpperCatAdministration:
    """Profile Manager class. For managing database interactions."""

    @staticmethod
    def insert_upperCat(upperCat: UpperCatObject) -> UpperCatObject:
        """Create a UpperCatObject."""
        with db_connector as db:
            cnx = db._cnx
            return UpperCatMapper.insert(cnx=cnx, object=upperCat)

    @staticmethod
    def get_upperCats() -> UpperCatObject:
        """Returns UpperCats by id."""
        with db_connector as db:
            cnx = db._cnx
            return UpperCatMapper.find_all(cnx=cnx)

    @staticmethod
    def delete_upperCat(upperCat: int) -> UpperCatObject:
        """Returns UpperCats by id."""
        with db_connector as db:
            cnx = db._cnx
            return UpperCatMapper.delete(cnx=cnx, upperCat=upperCat)

    @staticmethod
    def update_upperCat(upperCat: UpperCatObject) -> UpperCatObject:
        """Returns UpperCats by id."""
        with db_connector as db:
            cnx = db._cnx
            return UpperCatMapper.update(cnx=cnx, upperCat=upperCat)
