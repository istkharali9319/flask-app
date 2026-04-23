from flask import jsonify, request

from app.services.user_service import UserService
from app.utils.response import success_response,error_response
from app.repositories.user_repo import UserRepository
from flask_jwt_extended import jwt_required, get_jwt_identity

@jwt_required()
def get_users():
    users = UserService.list_users()
    return success_response(users,"User Fetched successfully")

def create_user():
    
    payload = request.get_json(silent=True) or {}
    errors = []
    username = payload.get("username")
    email = payload.get("email")
    password = payload.get("password")
    status= payload.get("status") or 0
    if not username:
        errors.append("Username is required!")
    if not email:
        errors.append("Email is required!")
    if not password:
        errors.append("Password is required!")

    existing_user = UserRepository.get_by_email(email)
    if existing_user:
        errors.append("Email already exixts!")

    if errors:
        return error_response("Validation Failed!",422,errors)
   
    try:
        user = UserService.create_user(payload)
        return success_response(user,"user Created successfully",201)
    except ValueError as exc:
        return error_response(str(exc),400)
        # return jsonify({"error": str(exc),"payload":payload}), 400
@jwt_required()
def update_user(id):
    try:
        payload = request.get_json(silent=True) or {}
        user = UserService.update_user(payload,id)
        if not user:
            return error_response("User not found",404)

        return success_response(user,"User updated successfully")
    except ValueError as exc:
        return error_response("Something went wrong",500)

@jwt_required()
def delete_user(id):
    try:
        user = UserService.delete_user(id)
        if not user:
            return error_response("User not found",404)
        return success_response([],'User Deleted successfully')
    except ValueError as exc:
        return error_response("Something went wrong",500)
