from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app.models.user import Base

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    full_name = Column(String(100), nullable=True)
    bio = Column(Text, nullable=True)
    birth_date = Column(Date, nullable=True)
    avatar_url = Column(String(255), nullable=True)
    location = Column(String(100), nullable=True)

    # Define relationship to User model
    user = relationship("User", backref="profile", uselist=False)

    def __repr__(self):
        return f"<Profile(user_id={self.user_id}, full_name='{self.full_name}')>"