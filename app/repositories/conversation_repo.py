from app.models.conversation import Conversation
from app.models.message import Message


class ConversationRepository:
    @staticmethod
    def get_all_by_user(user_id):
        return (
            Conversation.query.filter_by(user_id=user_id)
            .order_by(Conversation.updated_at.desc(), Conversation.id.desc())
            .all()
        )

    @staticmethod
    def get_by_id(conversation_id):
        return Conversation.query.get(conversation_id)

    @staticmethod
    def get_messages(conversation_id):
        return (
            Message.query.filter_by(conversation_id=conversation_id)
            .order_by(Message.created_at.asc(), Message.id.asc())
            .all()
        )
