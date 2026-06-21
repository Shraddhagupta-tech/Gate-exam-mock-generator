from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.db_connection import Base

class Topic(Base):
    __tablename__ = "topic"

    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey("subject.id"))
    name = Column(String(50))
    topic_code=Column(String(50))
    weightage=Column(Integer)
    