from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from app.database.db_connection import Base

class QuestionOption(Base):
    __tablename__ = "questionoption"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("question.id"))

    option_text = Column(Text, nullable=False)
    is_correct = Column(Boolean, nullable=False)