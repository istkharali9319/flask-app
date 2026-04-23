from flask import Blueprint

from app.controllers.user_controller import create_user, get_users,update_user,delete_user

user_bp = Blueprint("users", __name__, url_prefix="/api/users")

user_bp.route("/", methods=["GET"])(get_users)
user_bp.route("/create", methods=["POST"])(create_user)
user_bp.route("/update/<int:id>",methods=["PUT"])(update_user)
user_bp.route("/delete/<int:id>",methods=["DELETE"])(delete_user)
