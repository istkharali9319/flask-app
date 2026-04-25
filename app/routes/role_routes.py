from flask import Blueprint
from app.controllers.role_controller import get_roles,create_role,delete_role,update_role
role_bp = Blueprint("role",__name__,url_prefix="/api/roles")

role_bp.route('/',methods=["GET"])(get_roles)
role_bp.route('/create',methods=["POST"])(create_role)
role_bp.route('/delete/<int:id>',methods=["DELETE"])(delete_role)
role_bp.route('/update/<int:id>',methods=["PUT"])(update_role)