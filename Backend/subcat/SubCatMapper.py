from Backend.core.mapper import Mapper
from .SubCatBO import SubCatObject
from Backend.configs.base import db_connector


class SubCatMapper(Mapper):

    def insert(cnx: db_connector, object: SubCatObject) -> SubCatObject:
        """Creates a new Upper Category."""

        cursor = cnx.cursor(buffered=True)
        command = """
        INSERT INTO `ordersystem_db`.`sub_cat`
        (`subcat_name`,`upper_cat`)
        VALUES(%s,%s);
        """
        cursor.execute(command, (
            object.sub_category,
            object.upper_category,))

        cursor.execute("SELECT MAX(id) FROM upper_cat")
        max_id = cursor.fetchone()[0]
        object.id_ = max_id

        cnx.commit()
        cursor.close()
        return object

    def find_all(cnx: db_connector, upperCat: int) -> SubCatObject:
        """Get All Upper Categories."""
        result = []

        cursor = cnx.cursor(buffered=True)
        command = """
        SELECT id, subcat_name
        FROM `ordersystem_db`.`sub_cat`
        WHERE upper_cat IN(
                SELECT id from `ordersystem_db`.`upper_cat`
                WHERE id=%s)
        """

        cursor.execute(command,(upperCat,))
        tuples = cursor.fetchall()

        for (id, subcat_name) in tuples:
            subCat = SubCatObject(
                id_=id,
                sub_category=subcat_name,
            )
            result.append(subCat)

        cnx.commit()
        cursor.close()

        return result

    def delete(cnx: db_connector, subCat: int):
        """Get All Upper Categories."""

        cursor = cnx.cursor(buffered=True)
        command = """
        DELETE FROM `ordersystem_db`.`sub_cat`
        WHERE id=%s
        """

        try:
            cursor.execute(command, (subCat,))
        except Exception:
            print("Category does not exist!")

        cnx.commit()
        cursor.close()

    def update(cnx: db_connector, subCat: SubCatObject) -> SubCatObject:
        """Get All Upper Categories."""

        cursor = cnx.cursor(buffered=True)
        command = """
        UPDATE `ordersystem_db`.`sub_cat`
        SET`subcat_name` = %s WHERE `id` = %s;
        """

        cursor.execute(command,(subCat.sub_category, subCat.id_))

        cnx.commit()
        cursor.close()

        return subCat


