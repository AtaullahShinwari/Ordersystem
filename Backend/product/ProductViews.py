from Backend.configs.base import api
from .ProductMarshalling import product_marshalling
from .ProductBO import ProductObject
from .ProductAdministration import ProductAdministration
from Backend.core.auth import AuthView


""""Namespace prefix Product for APIs."""
namespace = api.namespace(
    "/product",
    description="Namespace for product APIs."
)


@namespace.route("/")
class ProductOperationAPI(AuthView):
    """Basic API for profile."""
    @api.marshal_with(product_marshalling, code=201)
    @api.expect(product_marshalling)
    def get(self) -> dict:
        """Get a product by id"""
        product = ProductAdministration.get_product_by_id(product=self.product.id_)
        return product

    @api.marshal_with(product_marshalling, code=201)
    @api.expect(product_marshalling)
    def post(self) -> dict:
        """Create product Endpoint."""
        product = ProductObject(**api.payload)
        product = ProductAdministration.insert_product(product=self.product.id_)
        return product

    @api.marshal_with(product_marshalling, code=201)
    @api.expect(product_marshalling)
    def delete(self) -> dict:
        """Delete product Endpoint."""
        ProductAdministration.delete_product(product=self.product.id_)
        return '', 200

@namespace.route("/<string:name")
class ProductAPI(AuthView):
    """Basic API for profile."""
    @api.marshal_with(product_marshalling, code=201)
    @api.expect(product_marshalling)
    def get(self, name) -> dict:
        """Get a product by name"""
        prd = ProductAdministration.get_product_by_name(name)
        return prd

@namespace.route("/productid/<int:product>")
class ProductDeleteAPI(AuthView):
    @api.marshal_with(product_marshalling, code=201)
    @api.expect(product_marshalling)
    def delete(self, product: int) -> dict:
        """Delete Product Endpoint."""
        ProductAdministration.delete_product(product=product)
        return '', 200
