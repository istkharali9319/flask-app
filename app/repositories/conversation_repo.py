from app.extensions import db
from app.models.user import User


class ConversationRepository:
    @staticmethod
    def get_all():
        return User.query.order_by(User.id.asc()).all()
        
