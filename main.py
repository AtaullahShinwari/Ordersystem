from flask import Flask, Blueprint
from flask_cors import CORS
from Backend.configs import BaseConfigs
from Backend.configs.base import api
from dotenv import load_dotenv

from Backend.uppercat.UpperCatViews import namespace as uppercat_namespace
from Backend.subcat.SubCatViews import namespace as subcat_namespace
from Backend.order.OrderViews import namespace as order_namespace

load_dotenv()


def create_app(config: BaseConfigs = BaseConfigs) -> Flask:
    """Return Flask app for project initialization."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    blueprint: Blueprint = Blueprint("api", __name__, url_prefix="/api")
    CORS(app, resources=r'/api/*', supports_credentials=True)
    init_lazily(blueprint)
    app.register_blueprint(blueprint)
    init_routes()

    return app


def init_lazily(blueprint: Blueprint) -> None:
    """Lazy init."""
    api.init_app(blueprint)


def init_routes() -> None:
    """Init Routes by using namespaces."""
    api.add_namespace(uppercat_namespace)
    api.add_namespace(subcat_namespace)

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
