from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSONB
from app.database.db_connection import Base

class MockAnalytics(Base):
    __tablename__ = "mockanalytics"

    id = Column(Integer, primary_key=True)

    attempt_id = Column(Integer)
    time_per_question = Column(Integer)
    accuracy_per_topic = Column(JSONB)