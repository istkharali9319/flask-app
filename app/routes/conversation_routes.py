from flask import Blueprint

from app.controllers.conversation_controller import get_conversations,create_conversation

conversation_bp = Blueprint("conversation", __name__, url_prefix="/api/conversations")

conversation_bp.route("/chat", methods=["POST"])(create_conversation)
# user_bp.route("/create", methods=["POST"])(create_user)
# user_bp.route("/update/<int:id>",methods=["PUT"])(update_user)
# user_bp.route("/delete/<int:id>",methods=["DELETE"])(delete_user)
