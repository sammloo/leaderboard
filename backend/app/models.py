from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(db.Model):
    __tablename__ = "user"

    id: so.Mapped[UUID] = so.mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: so.Mapped[str] = so.mapped_column(sa.String(64))
    age: so.Mapped[int] = so.mapped_column(sa.Integer)
    points: so.Mapped[int] = so.mapped_column(sa.Integer, default=0, index=True)
    address: so.Mapped[str] = so.mapped_column(sa.String(128))

    is_deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<User {self.name}, Age {self.age}, Points {self.points}>"

class Winner(db.Model):
    __tablename__ = "winner"

    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    user_id: so.Mapped[UUID] = so.mapped_column(sa.ForeignKey("user.id"), nullable=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64))
    points: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=True)
    timestamp: so.Mapped[sa.DateTime] = so.mapped_column(sa.DateTime, default=sa.func.current_timestamp())

    def __repr__(self):
        return f"<Winner {self.id}, User {self.user_id}, Points {self.points}>"
