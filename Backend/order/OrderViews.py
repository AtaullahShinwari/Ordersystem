from app.apps.core.auth import AuthView
from app.configs.base import api
from. OrderMarshalling import order_marshalling
from .OrderBO import OrderObject
from .OrderAdministration import OrderAdministration


namespace = api.namespace(
    "/order",
    description="Namespace for order APIs."
)

@namespace.route("/")
class OrderOperations(AuthView):
    @namespace.marshal_with(order_marshalling)
    def get(self):
        order_list = OrderAdministration.get_all_orders()
        return order_list
    
    @namespace.marshal_with(order_marshalling)
    def put(self, id_: int) -> dict:
        order=OrderObject(**api.payload)
        order=id_
        order=OrderAdministration.update(order=order)
        return order

