from app.apps.core.business_object import BusinessObject


class OrderObject(BusinessObject):
    """Class for Orderdata."""
    def __init__(self, quantity: int, annotation: str, tablenumber: int, 
                    product_id: int, id_: int = 0):
        self.quantity = quantity
        self.annotation = annotation
        self.tablenumber = tablenumber
        self.product_id = product_id

        super().__init__(id_=id_)
