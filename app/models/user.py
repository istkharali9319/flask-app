from app.extensions import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120) ,nullable=False)
    status = db.Column(db.Boolean,nullable=False)
    # Add role of the user

    role_id=db.Column(db.Integer,db.ForeignKey("roles.id"),nullable=True)

    # add relationship
    role = db.relationship("Role",back_populates="users")
    created_at = db.Column(db.DateTime,default = datetime.utcnow)
    updated_at = db.Column(db.DateTime,default = datetime.utcnow,onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "status":self.status
        }
