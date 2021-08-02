from Backend.core.business_object import BusinessObject


class ProductObject(BusinessObject):
    """Class for Product."""
    def __init__(self, name: str,
                price: float, description: str, menu_id:int, id_=0):
        self.name = name
        self.price = price
        self.description = description
        self.menu_id= menu_id

        super().__init__(id_=id_)