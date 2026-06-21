from sqlalchemy import Column, Integer, String
from app.database.db_connection import Base

class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)