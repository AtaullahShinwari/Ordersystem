from Backend.core.businessobject import BusinessObject


class UpperCatObject(BusinessObject):
    """Class for Persondata."""
    def __init__(self, upper_category: str, id_: int = 0):
        self.upper_category = upper_category

        super().__init__(id_=id_)
