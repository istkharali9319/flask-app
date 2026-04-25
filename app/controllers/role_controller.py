from flask import jsonify, request

from app.services.role_service import RoleService
from app.utils.response import success_response,error_response
from app.repositories.role_repo import RoleRepository
from flask_jwt_extended import jwt_required, get_jwt_identity

# @jwt_required()
def get_roles():
    roles = RoleService.list_roles()
    return success_response(roles,"Roles Fetched successfully")

def create_role():
    payload = request.get_json(silent=True) or {}
    errors = []
    name = payload.get('name')
    if not name:
        errors.append("Role name is required!")
   
    existing_role = RoleRepository.get_by_role(name)
    if existing_role:
        errors.append("Role already exixts!")

    if errors:
        return error_response("Validation Failed!",422,errors)
    
    try:
        role = RoleService.create_role(payload)
        return success_response(role,"Role Created successfully",201)
    except ValueError as exc:
        return error_response(str(exc),400)

        # return jsonify({"error": str(exc),"payload":payload}), 400
        
# @jwt_required()
def update_role(id):
    try:
        payload = request.get_json(silent=True) or {}
        role = RoleService.update_role(payload,id)
        if not role:
            return error_response("Role not found",404)

        return success_response(role,"Role updated successfully")
    except ValueError as exc:
        return error_response("Something went wrong",500)

# @jwt_required()
def delete_role(id):
    try:
        if id == 1:
            return error_response("The Super Admin role cannot be deleted.",403)

        role = RoleService.delete_role(id)
        if not role:
            return error_response("Role not found",404)
        return success_response([],'Role Deleted successfully')
    except ValueError as exc:
        return error_response("Something went wrong",500)
