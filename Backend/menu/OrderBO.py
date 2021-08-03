from Backend.core.businessobject import BusinessObject


class OrderObject(BusinessObject):
    """Class for Persondata."""
    def __init__(self, upper_category: str,
                subcategory: str, id_: int = 0):
        self.upper_category = upper_category
        self.subcategory = subcategory

        super().__init__(id_=id_)
