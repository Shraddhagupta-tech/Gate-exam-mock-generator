from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, Index
from app.database.db_connection import Base

class MockQuestion(Base):
    __tablename__ = "mockquestion"

    id = Column(Integer, primary_key=True)

    mocktest_id = Column(Integer, ForeignKey("mocktest.id"), index=True)
    question_id = Column(Integer, ForeignKey("question.id"))

    question_order = Column(Integer)


    __table_args__ = (
        UniqueConstraint("mocktest_id", "question_order"),
        UniqueConstraint("mocktest_id", "question_id"),
        Index("idx_mocktest", "mocktest_id"),
    )