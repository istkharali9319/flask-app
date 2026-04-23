from flask import Blueprint

from app.controllers.profile_controller import get_profile

profile_bp = Blueprint("profile", __name__, url_prefix="/api/profile")

profile_bp.route("/", methods=["GET"])(get_profile)
