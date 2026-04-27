from flask import jsonify, request

from app.services.ai_service import AiService
from app.services.conversation_service import ConversationService
from app.utils.response import success_response,error_response
from app.repositories.conversation_repo import  ConversationRepository
from flask_jwt_extended import jwt_required, get_jwt_identity

@jwt_required()
def get_conversations():
    users = UserService.list_users()
    return success_response(users,"User Fetched successfully")

@jwt_required()
def create_conversation():
    current_user = get_jwt_identity()

    payload = request.get_json(silent=True) or {}
    errors = []
    user_message = payload.get("title")
    if not user_message:
        errors.append("User message is required!")

    if errors:
        return error_response("Validation Failed!",422,errors)
    try:
        ai_response = AiService.call_openai_api(user_message)
        conversation_id = payload.get("conversation_id") or None
        conversation = ConversationService.save_conversation(
            user_message,
            ai_response,
            conversation_id,
            current_user)
        return success_response(conversation,"Response generated successfully",201)
    except ValueError as exc:
        return error_response(str(exc),400)
        return jsonify({"error": str(exc),"payload":payload}), 400
        
