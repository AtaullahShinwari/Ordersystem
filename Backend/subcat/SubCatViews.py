from Backend.configs.base import api
from .SubCatMarshalling import subcat_marshalling
from .SubCatBO import SubCatObject
from .SubCatAdministration import SubCatAdministration
from flask_restx import Api, Resource, fields

""""Namespace prefix SubCat for APIs."""
namespace = api.namespace(
    "/SubCat",
    description="Namespace for SubCat APIs."
)

@namespace.route("/<int:upperCat_id>")
class AllSubCatOperationAPI(Resource):
    """Basic API for Upper Category."""
    @api.marshal_with(subcat_marshalling, code=201)
    @api.expect(subcat_marshalling)
    def get(self, upperCat_id: int) -> dict:
        """Get a SubCat by google_user_id"""
        SubCat = SubCatAdministration.get_subCats(upperCat=upperCat_id)
        return SubCat

    @api.marshal_with(subcat_marshalling, code=201)
    @api.expect(subcat_marshalling)
    def post(self, upperCat_id: int) -> dict:
        """Create SubCat Endpoint."""
        subCat_ = SubCatObject(**api.payload)
        subCat = SubCatAdministration.insert_subCat(upperCat=upperCat_id,subCat=subCat_)
        return subCat

@namespace.route("/<int:subCat_id>")
class SubCatOperationAPI(Resource):
    """Basic API for specific Upper Category."""
    @api.marshal_with(subcat_marshalling, code=201)
    @api.expect(subcat_marshalling)
    def delete(self, subCat_id: int) -> dict:
        """Delete SubCat Endpoint."""
        SubCatAdministration.delete_subCat(subCat=subCat_id)
        return '', 200

    @api.marshal_with(subcat_marshalling, code=201)
    @api.expect(subcat_marshalling)
    def put(self, subCat_id: int) -> dict:
        """Delete SubCat Endpoint."""
        subCat = SubCatObject(**api.payload)
        subCat.id_ = subCat_id
        subCat = SubCatAdministration.update_subCat(subCat=subCat)
        return subCat
