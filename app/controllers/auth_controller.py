from flask import jsonify, request
from app.models.user import User
from app.services.auth_service import AuthService
from app.services.user_service import UserService
from app.utils.response import success_response,error_response
from flask_jwt_extended import create_access_token

def login():
    try:
        payload = request.get_json(silent=True) or {}
        errors = []
        email = payload.get("email")
        password = payload.get("password")

        if not email:
            errors.append("Email is required")

        if not password:
            errors.append("Password is required")

        if errors:
            return error_response("Validation Failed!",422,errors)

        user =  AuthService.login(email,password)
        if not user:
            return error_response("Invalid credentials",401)
        
        verify_password = UserService.verify_password(password,user.password)
        token = create_access_token(identity=user.id)
        user.token = token
        return success_response({
            "username":user.username,
            "user_id": user.id,
            "email": user.email,
            "access_token": token
        }, "Login successful")

    except ValueError as exc:
        return error_response("Internal server error",500)


    
