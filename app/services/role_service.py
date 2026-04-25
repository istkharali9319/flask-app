from app.repositories.role_repo import RoleRepository
import bcrypt

class RoleService:
    @staticmethod
    def list_roles():
        return [role.to_dict() for role in RoleRepository.get_all()]

    @staticmethod
    def create_role(payload):
        name = payload.get("name")
        role = RoleRepository.create(name=name)
        return role.to_dict()

    @staticmethod
    def update_role(payload,role_id):
        name = payload.get("name")
        role = RoleRepository.update(role_id,name)
        if role == None:
            return None

        return role.to_dict()

    @staticmethod
    def delete_role(role_id):
        return RoleRepository.delete(role_id)
