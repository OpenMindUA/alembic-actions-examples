from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.models.user import Base

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Define relationship to User model
    user = relationship("User", backref="posts")

    # Many-to-many relationship with tags
    tags = relationship("Tag", secondary="post_tags", back_populates="posts")

    def __repr__(self):
        return f"<Post(title='{self.title}', user_id={self.user_id})>"