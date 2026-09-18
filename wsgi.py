from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

# Shared extension instances - every module imports these, never creates its own
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    # Register one blueprint per module.
    # Each teammate builds inside their own file in app/routes/
    # and just needs to define `bp = Blueprint(...)` there.
    from app.routes.auth import bp as auth_bp
    from app.routes.customers import bp as customers_bp
    from app.routes.leads import bp as leads_bp
    from app.routes.deals import bp as deals_bp
    from app.routes.tasks import bp as tasks_bp
    from app.routes.dashboard import bp as dashboard_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(customers_bp)
    app.register_blueprint(leads_bp)
    app.register_blueprint(deals_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(dashboard_bp)

    with app.app_context():
        from app import models  # noqa: F401 - registers tables before create_all
        try:
            db.create_all()
        except Exception as exc:
            app.logger.warning("create_all skipped: %s", exc)

    return app
