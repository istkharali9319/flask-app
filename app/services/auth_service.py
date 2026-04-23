from app.models.user import User
import bcrypt

class AuthService:
    @staticmethod
    def login(email,password):
        user = User.query.filter_by(email=email).first()
        return user

