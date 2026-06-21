from sqlalchemy import Column, Integer, String, Enum, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.database.db_connection import Base
from app.models.user import User

class MockTest(Base):
    __tablename__ = "mocktest"

    id = Column(Integer, primary_key=True,autoincrement=True)

    title = Column(String(100))
    exam_type = Column(Enum("CSE","DA", name="mock_exam_type"))

    created_by = Column(Integer, ForeignKey("user.id"))

    total_marks = Column(Integer, default=100)
    duration_minutes = Column(Integer, default=180)

    is_generated = Column(Boolean,default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())