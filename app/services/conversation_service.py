
from app.extensions import db
from app.models.conversation import Conversation
from app.models.message import Message

class ConversationService:
    @staticmethod
    def save_conversation(user_message,ai_response,conversation_id,user_id):
        # save conversation if conversation_id is not present
        if not conversation_id:
            conversation = Conversation(
                title = user_message,
                user_id = user_id
            )
            db.session.add(conversation)
            db.session.commit()
            conversation_id = conversation.id

        # save user message
        message = Message(
            conversation_id = conversation_id,
            role = "user",
            content = user_message
        )

        db.session.add(message)

        # save ai message

        ai_message = Message(
            conversation_id = conversation_id,
            role = "assistant",
            content = ai_response
        )

        db.session.add(ai_message)
        db.session.commit()
        return conversation.to_dict() 

