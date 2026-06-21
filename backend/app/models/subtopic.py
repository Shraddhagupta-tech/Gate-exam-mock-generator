from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.db_connection import Base

class Subtopic(Base):
    __tablename__ = "subtopic"

    id = Column(Integer, primary_key=True)
    name=Column(String(50))
    topic_id = Column(Integer, ForeignKey("topic.id"))
