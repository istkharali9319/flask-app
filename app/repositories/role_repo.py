from app.extensions import db
from app.models.role import Role

class RoleRepository:
    @staticmethod
    def get_all():
        return Role.query.order_by(Role.id.asc()).all()

    @staticmethod
    def create(name):
        role = Role(name=name)
        db.session.add(role)
        db.session.commit()
        return role
    
    @staticmethod
    def update(role_id, name=None):
        role = Role.query.get(role_id)
        if not role:
            return None
            
        role.name=name
        db.session.commit()
        return role

    @staticmethod
    def delete(role_id):
        role = Role.query.get(role_id)
        if role == None:
            return None
        
        db.session.delete(role)
        db.session.commit()
        return role

    @staticmethod
    def get_by_role(role):
        return Role.query.filter_by(name=role).first()

        
