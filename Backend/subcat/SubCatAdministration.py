from .SubCatMapper import SubCatMapper
from .SubCatBO import SubCatObject
from Backend.configs.base import db_connector


class SubCatAdministration:
    """Profile Manager class. For managing database interactions."""

    @staticmethod
    def insert_subCat(subCat: SubCatObject) -> SubCatObject:
        """Create a SubCatObject."""
        with db_connector as db:
            cnx = db._cnx
            return SubCatMapper.insert(cnx=cnx, object=subCat)

    @staticmethod
    def get_subCats(upperCat: int) -> SubCatObject:
        """Returns SubCats by id."""
        with db_connector as db:
            cnx = db._cnx
            return SubCatMapper.find_all(cnx=cnx, upperCat=upperCat)

    @staticmethod
    def delete_subCat(subCat: int) -> SubCatObject:
        """DeleteSubCats by id."""
        with db_connector as db:
            cnx = db._cnx
            return SubCatMapper.delete(cnx=cnx, subCat=subCat)

    @staticmethod
    def update_subCat(subCat: SubCatObject) -> SubCatObject:
        """updates SubCats by id."""
        with db_connector as db:
            cnx = db._cnx
            return SubCatMapper.update(cnx=cnx, subCat=subCat)
