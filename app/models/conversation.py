from app.extensions import db
from datetime import datetime


class Conversation(db.Model):
    __tablename__ = "conversations"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime,default = datetime.utcnow)
    updated_at = db.Column(db.DateTime,default = datetime.utcnow,onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    messages = db.relationship("Message", backref="conversation", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
        }
