from flask import Blueprint

from app.controllers.auth_controller import login

auth_bp = Blueprint("auth",__name__,url_prefix="/api/auth")

auth_bp.route("/login",methods=["POST"])(login)
# auth_bp.route("/forgot-password",methods=["GET"])(forgorPassword)
# auth_bp.route("/change-password",methods=["GET"])(resePasswprd)