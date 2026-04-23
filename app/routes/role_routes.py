from flask import Blueprint
from app.controllers.role_controller import ç
role_bp = Blueprint("role",__name__,url_prefix="/api/role")

role_bp.route('/',methods=["GET"])(get_roles)