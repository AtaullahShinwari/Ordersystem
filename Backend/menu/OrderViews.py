from Backend.configs.base import api
from .OrderMarshalling import order_marshalling
from .OrderBO import OrderObject
from .OrderAdministration import OrderAdministration
from flask_restx import Api, Resource, fields

""""Namespace prefix order for APIs."""
namespace = api.namespace(
    "/order",
    description="Namespace for order APIs."
)

@namespace.route("/")
class orderOperationAPI(Resource):
    """Basic API for profile."""
    @api.marshal_with(order_marshalling, code=201)
    @api.expect(order_marshalling)
    def get(self) -> dict:
        """Get a order by google_user_id"""
        order = OrderAdministration.get_order_by_id(order=self.order.id_)
        return order

    @api.marshal_with(order_marshalling, code=201)
    @api.expect(order_marshalling)
    def post(self) -> dict:
        """Create order Endpoint."""
        order = OrderObject(**api.payload)
        order = OrderAdministration.insert_order(order=self.order.id_)
        return order

    @api.marshal_with(order_marshalling, code=201)
    @api.expect(order_marshalling)
    def delete(self) -> dict:
        """Delete order Endpoint."""
        OrderAdministration.delete_order(order=self.order.id_)
        return '', 200