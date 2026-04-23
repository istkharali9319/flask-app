from app.extensions import db
from app.models.user import User


class UserRepository:
    @staticmethod
    def get_all():
        return User.query.order_by(User.id.asc()).all()

    @staticmethod
    def create(username, email,password,status):
        user = User(username=username, email=email,password=password,status=status)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def update(user_id, username=None, email=None ,password=None,status=None):
        user = User.query.get(user_id)
        if not user:
            return None
            
        if username is not None:
            user.username=username
        if status is not None:
            user.status=status

        db.session.commit()
        return user
    @staticmethod
    def delete(user_id):
        user = User.query.get(user_id)
        if user == None:
            return None
        
        db.session.delete(user)
        db.session.commit()
        return user

    @staticmethod
    def get_by_email(email):
            return User.query.filter_by(email=email).first()

        
