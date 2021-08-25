from Backend.core.businessobject import BusinessObject


class ProductObject(BusinessObject):
    """Class for Product."""
    def __init__(self, name: str,
                price: float, description: str, sub_id:int, id_=0):
        self.name = name
        self.price = price
        self.description = description
        self.sub_id= sub_id

        super().__init__(id_=id_)