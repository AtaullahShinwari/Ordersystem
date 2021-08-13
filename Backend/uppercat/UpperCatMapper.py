from Backend.core.mapper import Mapper
from .UpperCatBO import UpperCatObject
from Backend.configs.base import db_connector


class UpperCatMapper(Mapper):

    def insert(cnx: db_connector, object: UpperCatObject) -> UpperCatObject:
        """Creates a new Upper Category."""

        cursor = cnx.cursor(buffered=True)
        command = """
        INSERT INTO `ordersystem_db`.`upper_cat`
        (`uppercat_name`)
        VALUES(%s);
        """
        cursor.execute(command, (
            object.upper_category,))

        cursor.execute("SELECT MAX(id) FROM upper_cat")
        max_id = cursor.fetchone()[0]
        object.id_ = max_id

        cnx.commit()
        cursor.close()
        return object

    def find_all(cnx: db_connector) -> UpperCatObject:
        """Get All Upper Categories."""
        result = []

        cursor = cnx.cursor(buffered=True)
        command = """
        SELECT `id`,`uppercat_name`
        FROM `ordersystem_db`.`upper_cat`;
        """

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, uppercat_name) in tuples:
            upperCat = UpperCatObject(
                id_=id,
                upper_category=uppercat_name
            )
            result.append(upperCat)

        cnx.commit()
        cursor.close()

        return result

    def delete(cnx: db_connector, upperCat: int):
        """Get All Upper Categories."""

        cursor = cnx.cursor(buffered=True)
        command = """
        DELETE FROM `ordersystem_db`.`upper_cat`
        WHERE id=%s;
        """

        try:
            cursor.execute(command, (upperCat))
        except Exception:
            print("Category does not exist!")

        cnx.commit()
        cursor.close()

    def update(cnx: db_connector, upperCat: UpperCatObject) -> UpperCatObject:
        """Get All Upper Categories."""

        cursor = cnx.cursor(buffered=True)
        command = """
        UPDATE `ordersystem_db`.`upper_cat`
        SET
        `uppercat_name` = %s
        WHERE `id` = %s;
        """

        cursor.execute(command,(upperCat.upper_category, upperCat.id_))

        cnx.commit()
        cursor.close()

        return upperCat


