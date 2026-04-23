from flask import jsonify, request
from app.utils.response import success_response, error_response 
from app.services.category_service import CategoryService


def get_categories():
    return jsonify(CategoryService.list_users()), 200


def create_user():
    payload = request.get_json(silent=True) or {}

    try:
        category = CategoryService.create_category(payload)
        return jsonify(category), 201
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
