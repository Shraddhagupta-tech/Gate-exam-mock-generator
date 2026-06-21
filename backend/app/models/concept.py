from sqlalchemy import Column, Integer, String, Enum, ForeignKey, UniqueConstraint
from app.database.db_connection import Base

class Concept(Base):
    __tablename__ = "concept"

    id = Column(Integer, primary_key=True)

    concept_code = Column(String(50))
    subtopic_id = Column(Integer, ForeignKey("subtopic.id"))
    name=Column(String(50))
    exam_type = Column(Enum("CSE","DA", name="exam_type"))
    
    weightage = Column(Integer)

    __table_args__ = (
        UniqueConstraint("concept_code", "exam_type"),
    )
