from app.repositories.user_repo import UserRepository
import bcrypt

class UserService:
    @staticmethod
    def list_users():
        return [user.to_dict() for user in UserRepository.get_all()]

    @staticmethod
    def create_user(payload):
        username = payload.get("username")
        email = payload.get("email")
        password = UserService.hash_password(payload.get("password"))
        status = payload.get("status")

        if not username or not email:
            raise ValueError("username and email are required")
        
        existing_user = UserRepository.get_by_email(email)
        if existing_user:
         raise ValueError("Email already exists")

        user = UserRepository.create(username=username, email=email,password=password,status=status)
        return user.to_dict()

    @staticmethod
    def update_user(payload,user_id):
        username = payload.get("username")
        status = payload.get("status")
        user = UserRepository.update(user_id,username,None,None,status)
        if user == None:
            return None

        return user.to_dict()

    @staticmethod
    def delete_user(user_id):
        return UserRepository.delete(user_id)

    @staticmethod
    def hash_password(password: str):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    @staticmethod
    def verify_password(password:str,hash_password:str):
        return bcrypt.checkpw(password.encode(),hash_password.encode())

