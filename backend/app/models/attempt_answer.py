from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Index, String
from app.database.db_connection import Base

class AttemptAnswer(Base):
    __tablename__ = "attemptanswer"

    id = Column(Integer, primary_key=True)

    attempt_id = Column(Integer, ForeignKey("studentattempt.id"), index=True)
    question_id = Column(Integer, ForeignKey("question.id"))

    answer_numeric = Column(DECIMAL(10,4))
    selected_option = Column(String)

    __table_args__ = (
        Index("idx_attempt", "attempt_id"),
        Index("idx_attempt_q", "attempt_id", "question_id"),
    )
    