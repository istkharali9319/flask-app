
from app.extensions import db
from app.models.conversation import Conversation
from app.models.message import Message
from app.repositories.conversation_repo import ConversationRepository
from datetime import datetime

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
        else:
            conversation = ConversationRepository.get_by_id(conversation_id)
            if not conversation or conversation.user_id != user_id:
                raise ValueError("Conversation not found")

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
        conversation.updated_at = datetime.utcnow()
        db.session.commit()
        return conversation.to_dict() 

    @staticmethod
    def list_conversations(user_id):
        conversations = ConversationRepository.get_all_by_user(user_id)
        results = []

        for conversation in conversations:
            messages = ConversationRepository.get_messages(conversation.id)
            latest_message = messages[-1] if messages else None
            results.append(
                {
                    **conversation.to_dict(),
                    "preview": latest_message.content[:120] if latest_message else "",
                    "message_count": len(messages),
                }
            )

        return results

    @staticmethod
    def get_conversation_messages(conversation_id, user_id):
        conversation = ConversationRepository.get_by_id(conversation_id)
        if not conversation or conversation.user_id != user_id:
            raise ValueError("Conversation not found")

        messages = ConversationRepository.get_messages(conversation_id)
        return {
            **conversation.to_dict(),
            "messages": [message.to_dict() for message in messages],
        }
