from sqlalchemy import Column, Integer, ForeignKey, Enum, TIMESTAMP, Index
from app.database.db_connection import Base

class StudentAttempt(Base):
    __tablename__ = "studentattempt"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("user.id"), index=True)
    mocktest_id = Column(Integer, ForeignKey("mocktest.id"))

    score = Column(Integer, default=0)

    started_at = Column(TIMESTAMP)
    completed_at = Column(TIMESTAMP)

    status = Column(Enum("in_progress","completed","submitted", name="attempt_status"))

    __table_args__ = (
        Index("idx_user_attempt", "user_id"),
    )