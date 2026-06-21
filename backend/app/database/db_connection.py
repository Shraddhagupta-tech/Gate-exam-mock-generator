from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from sqlalchemy.engine import URL
import os
from dotenv import load_dotenv
load_dotenv()

url = URL.create(
    drivername="postgresql",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

engine=create_engine(url)

SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()




Base=declarative_base()