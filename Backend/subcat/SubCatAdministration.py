from .SubCatMapper import SubCatMapper
from .SubCatBO import SubCatObject
from Backend.configs.base import db_connector


class SubCatAdministration:
    """Profile Manager class. For managing database interactions."""

    @staticmethod
    def insert_SubCat(SubCat: SubCatObject) -> SubCatObject:
        """Create a SubCatObject."""
        with db_connector as db:
            cnx = db._cnx
            return SubCatMapper.insert(cnx=cnx, object=SubCat)

    @staticmethod
    def get_SubCats() -> SubCatObject:
        """Returns SubCats by id."""
        with db_connector as db:
            cnx = db._cnx
            return SubCatMapper.find_all(cnx=cnx)

    @staticmethod
    def delete_SubCat(SubCat: int) -> SubCatObject:
        """Returns SubCats by id."""
        with db_connector as db:
            cnx = db._cnx
            return SubCatMapper.delete(cnx=cnx, SubCat=SubCat)

    @staticmethod
    def update_SubCat(SubCat: SubCatObject) -> SubCatObject:
        """Returns SubCats by id."""
        with db_connector as db:
            cnx = db._cnx
            return SubCatMapper.update(cnx=cnx, SubCat=SubCat)
