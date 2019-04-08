import logging
import yaml

import connexion
from connexion.resolver import RestyResolver

import config
import db

logger = logging.getLogger(__name__)


def create_app():
    conn_app = connexion.App(
        "preferences",
        specification_dir="./spec/")

    with open("spec/api.spec.yaml", "rb") as fp:
        spec = yaml.safe_load(fp)

    conn_app.add_api(
        spec,
        arguments={"title": "Insights Preferences"},
        resolver=RestyResolver("api"),
        validate_responses=True,
        strict_validation=True,
        base_path="",
    )

    flask_app = conn_app.app

    flask_app.config["SQLALCHEMY_ECHO"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = config.db_uri
    flask_app.config["SQLALCHEMY_POOL_SIZE"] = config.db_pool_size
    flask_app.config["SQLALCHEMY_POOL_TIMEOUT"] = config.db_pool_timeout

    db.init_app(flask_app)

    return flask_app
