from Backend.configs.base import api
from .UpperCatMarshalling import upperCat_marshalling
from .UpperCatBO import UpperCatObject
from .UpperCatAdministration import UpperCatAdministration
from flask_restx import Api, Resource, fields

""""Namespace prefix UpperCat for APIs."""
namespace = api.namespace(
    "/UpperCat",
    description="Namespace for UpperCat APIs."
)

@namespace.route("/")
class AllUpperCatOperationAPI(Resource):
    """Basic API for Upper Category."""
    @api.marshal_with(upperCat_marshalling, code=201)
    @api.expect(upperCat_marshalling)
    def get(self) -> dict:
        """Get a UpperCat by google_user_id"""
        upperCat = UpperCatAdministration.get_upperChats()
        return upperCat

    @api.marshal_with(upperCat_marshalling, code=201)
    @api.expect(upperCat_marshalling)
    def post(self) -> dict:
        """Create UpperCat Endpoint."""
        upperCat_ = UpperCatObject(**api.payload)
        upperCat = UpperCatAdministration.insert_upperCat(upperCat=upperCat_)
        return upperCat

@namespace.route("/<int:upperCat_id>")
class UpperCatOperationAPI(Resource):
    """Basic API for specific Upper Category."""
    @api.marshal_with(upperCat_marshalling, code=201)
    @api.expect(upperCat_marshalling)
    def delete(self, upperCat_id: int) -> dict:
        """Delete UpperCat Endpoint."""
        UpperCatAdministration.delete_upperCat(upperCat=upperCat_id)
        return '', 200

    @api.marshal_with(upperCat_marshalling, code=201)
    @api.expect(upperCat_marshalling)
    def put(self, upperCat_id: int) -> dict:
        """Delete UpperCat Endpoint."""
        UpperCatAdministration.update_upperCat(upperCat=upperCat_id)
        return '', 200
