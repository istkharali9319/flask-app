from flask import request, Response,stream_with_context

from app.services.ai_service import AiService
from app.services.conversation_service import ConversationService
from app.utils.response import success_response,error_response
from flask_jwt_extended import jwt_required, get_jwt_identity
import time


@jwt_required()
def get_conversations():
    current_user = get_jwt_identity()
    conversations = ConversationService.list_conversations(int(current_user))
    return success_response(conversations,"Conversations fetched successfully")

@jwt_required()
def get_conversation_messages(conversation_id):
    current_user = get_jwt_identity()
    try:
        conversation = ConversationService.get_conversation_messages(conversation_id, int(current_user))
        return success_response(conversation,"Conversation fetched successfully")
    except ValueError as exc:
        return error_response(str(exc),404)

@jwt_required()
def create_conversation():
    current_user = get_jwt_identity()

    payload = request.get_json(silent=True) or {}
    errors = []
    user_message = payload.get("prompt")
    provider = payload.get("provider")
    if not user_message:
        errors.append("Prompt is required!")
    if not provider:
        errors.append("Provider is required!")

    if errors:
        return error_response("Validation Failed!",422,errors)
    try:
        ai_response = AiService.call_ai_service(user_message,provider)
        conversation_id = payload.get("conversation_id") or None
        conversation = ConversationService.save_conversation(
            user_message,
            ai_response,
            conversation_id,
            int(current_user))
        return success_response(conversation,"Response generated successfully",201)
    except ValueError as exc:
        return error_response(str(exc),400)
        return jsonify({"error": str(exc),"payload":payload}), 400
    
@jwt_required()
def stream_conversation():
    current_user = get_jwt_identity()
    payload = request.get_json(silent=True) or {}

    user_message = payload.get("prompt")
    provider = payload.get("provider", "openai")
    conversation_id = payload.get("conversation_id")
    language = payload.get("language", "Python")

    if not user_message:
        return error_response("Prompt is required!", 422)

    system_prompt = (
        f"You are an expert AI Tutor for {language}. "
        "Provide clear code examples and explain logic step-by-step."
    )

    # ✅ shared variable
    full_response = []

    def generate():
        try:
            for chunk in AiService.call_ai_stream(user_message, provider, system_prompt):
                full_response.append(chunk)   # store pieces
                yield chunk
                time.sleep(0.05)

        except Exception as e:
            yield f"\n[e]: {str(e)}"

    response = Response(
        stream_with_context(generate()),
        content_type="text/plain"
    )

    # ✅ runs AFTER stream closes
    @response.call_on_close
    def save_after_stream():
        try:
            final_text = "".join(full_response)

            ConversationService.save_conversation(
                user_message,
                final_text,
                conversation_id,
                int(current_user)
            )

            print("✅ Conversation saved")

        except Exception as e:
            print("❌ DB Save Error:", e)

    return response
