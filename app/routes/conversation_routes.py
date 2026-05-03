from flask import Blueprint

from app.controllers.conversation_controller import (
    get_conversations,
    create_conversation,
    stream_conversation,
    get_conversation_messages,
)

conversation_bp = Blueprint("conversation", __name__, url_prefix="/api/conversations")

conversation_bp.route("", methods=["GET"])(get_conversations)
conversation_bp.route("/chat", methods=["POST"])(create_conversation)
conversation_bp.route('/stream',methods=["POST"])(stream_conversation)
conversation_bp.route("/<int:conversation_id>/messages", methods=["GET"])(get_conversation_messages)
# user_bp.route("/create", methods=["POST"])(create_user)
# user_bp.route("/update/<int:id>",methods=["PUT"])(update_user)
# user_bp.route("/delete/<int:id>",methods=["DELETE"])(delete_user)
