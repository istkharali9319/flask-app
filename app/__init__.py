import time

from flask import Flask, jsonify

from app.config import Config
from app.errors.handlers import register_error_handlers
from app.extensions import db, migrate, jwt
from app.routes.user_routes import user_bp
from app.routes.profile_routes import profile_bp
# from app.routes.category_routes import category_bp
from app.routes.auth_routes import auth_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(user_bp)
    register_error_handlers(app)

    # Import models for migrations
    from app.models.user import User

    @app.get("/")
    def index():
        return jsonify(
            {
                "message": "Istkhar Ali profile API is running",
                "service": "portfolio api",
                "role": "Senior Full Stack Engineer",
                "endpoints": ["/", "/health", "/api/profile/", "/api/users/", "/api/auth/login"],
            }
        )

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    # Remove db.create_all() - use Flask-Migrate instead
    # with app.app_context():
    #     last_error = None
    #     for _attempt in range(10):
    #         try:
    #             db.create_all()
    #             last_error = None
    #             break
    #         except Exception as exc:  # pragma: no cover
    #             last_error = exc
    #             time.sleep(2)
    #
    #     if last_error is not None:
    #         raise last_error

    return app
