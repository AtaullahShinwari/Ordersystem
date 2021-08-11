from Backend.core.businessobject import BusinessObject


class SubCatObject(BusinessObject):
    """Class for Persondata."""
    def __init__(self, sub_category: str, upper_category: int,  id_: int = 0):
        self.sub_category = sub_category
        self.upper_category = upper_category

        super().__init__(id_=id_)
