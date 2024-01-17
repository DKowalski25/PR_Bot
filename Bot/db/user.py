import datetime

from sqlalchemy import Column, Integer, VARCHAR, DATE

from .base import BaseModel


class User(BaseModel):
    """User table."""
    __tablename__ = 'users'

    # Telegram user id
    user_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    # Telegram user name
    user_name = Column(VARCHAR(32), nullable=False)
    # Registration date
    reg_date = Column(DATE, default=datetime.date.today())
    # Last update date
    upd_date = Column(DATE, onupdate=datetime.date.today())

    def __str__(self) -> str:
        return f'<User:{self.user_id}>'




