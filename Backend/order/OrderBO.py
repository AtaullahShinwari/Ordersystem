from Backend.core.businessobject import BusinessObject


class OrderObject(BusinessObject):
    """Class for Orderdata."""
    def __init__(self, quantity: int, annotation: str, table_: int, 
                    product: int, id_: int = 0):
        self.quantity = quantity
        self.annotation = annotation
        self.table_ = table_
        self.product = product

        super().__init__(id_=id_)
