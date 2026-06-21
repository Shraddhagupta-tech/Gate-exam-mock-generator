from sqlalchemy import Column, Integer, TIMESTAMP
from app.database.db_connection import Base

class TopicPerformance(Base):
    __tablename__ = "topicperformance"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)
    concept_id = Column(Integer)

    accuracy = Column(Integer)
    attempts = Column(Integer)
    last_updated = Column(TIMESTAMP)